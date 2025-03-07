import pyqrcode
import base64
from io import BytesIO
from django.views.decorators.csrf import csrf_exempt
from django_otp.plugins.otp_totp.models import TOTPDevice
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from django_otp.plugins.otp_totp.models import TOTPDevice
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
from .serializers import UserSerializer

User = get_user_model()

@csrf_exempt
@api_view(["GET"])
@permission_classes([AllowAny])
def generate_qr_code(request):
    try:
        secret = "JBSWY3DPEHPK3PXP"  # 🔹 Reemplaza con la clave secreta del usuario
        qr_data = f"otpauth://totp/TestApp?secret={secret}&issuer=TestApp"

        qr = pyqrcode.create(qr_data)
        buffer = BytesIO()
        qr.png(buffer, scale=5)
        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        return Response({"qr_code": f"data:image/png;base64,{qr_base64}"})
    except Exception as e:
        print("Error generando QR:", e)  # 🔹 Ver el error en la consola
        return Response({"error": "Error interno al generar el código QR"}, status=500)

@api_view(["POST"])
def login_user(request):
    email = request.data.get("email")
    password = request.data.get("password")
    otp_token = request.data.get("otp_token")  # 🔹 Código de Google Authenticator

    if not email or not password or not otp_token:
        return Response({"error": "Faltan datos"}, status=400)

    user = authenticate(username=email, password=password)
    if user is None:
        return Response({"error": "Credenciales incorrectas"}, status=400)

    try:
        device = TOTPDevice.objects.get(user=user, confirmed=True)
        if not device.verify_token(otp_token):
            return Response({"error": "Código 2FA incorrecto"}, status=400)
    except TOTPDevice.DoesNotExist:
        return Response({"error": "No se encontró dispositivo 2FA"}, status=400)

    return Response({"message": "Login exitoso", "token": "JWT-TOKEN-AQUÍ"})

@api_view(["POST"])
def register_user(request):
    username = request.data.get("username")
    email = request.data.get("email")
    password = request.data.get("password")

    if not username or not email or not password:
        return Response({"error": "Todos los campos son obligatorios"}, status=400)

    if User.objects.filter(email=email).exists():
        return Response({"error": "El correo ya está registrado"}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)

    # Crear el dispositivo OTP para el usuario
    device = TOTPDevice.objects.create(user=user, name="Google Authenticator")
    user.otp_device = device
    user.save()

    return Response({"message": "Usuario registrado correctamente"})
