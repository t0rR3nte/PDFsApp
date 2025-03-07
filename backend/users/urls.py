from django.urls import path
from .views import register_user, login_user, generate_qr_code

urlpatterns = [
    path('register/', register_user, name='register'),
    path("login/", login_user, name="login"),
    path("qr-code/", generate_qr_code, name="qr-code"),
]
