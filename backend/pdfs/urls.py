from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PDFDocumentViewSet

router = DefaultRouter()
router.register(r'pdfs', PDFDocumentViewSet, basename="pdf")

urlpatterns = [
    path("", include(router.urls)),
    path("pdfs/<int:pk>/approve/", PDFDocumentViewSet.as_view({"post": "approve"}), name="approve-pdf"),
]
