from rest_framework import serializers
from .models import PDFDocument

class PDFDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDFDocument
        fields = "__all__"
        read_only_fields = ["uploaded_by", "approved"]
