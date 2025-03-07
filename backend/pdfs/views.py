from rest_framework import viewsets, permissions
from rest_framework.response import Response
from .models import PDFDocument
from .serializers import PDFDocumentSerializer

class IsOperator(permissions.BasePermission):
    """Permite acceso solo a usuarios operadores"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_operator

class IsApprover(permissions.BasePermission):
    """Permite acceso solo a usuarios aprobadores"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_approver

class PDFDocumentViewSet(viewsets.ModelViewSet):
    """CRUD de PDFs con permisos"""
    queryset = PDFDocument.objects.all()
    serializer_class = PDFDocumentSerializer

    def get_permissions(self):
        if self.action in ["create", "update", "destroy"]:
            return [IsOperator()]
        elif self.action == "approve":
            return [IsApprover()]
        return [permissions.IsAuthenticated()]

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def approve(self, request, pk=None):
        """Aprobar un PDF (Solo Aprobadores)"""
        pdf = self.get_object()
        pdf.approved = True
        pdf.save()
        return Response({"message": "PDF aprobado"})
