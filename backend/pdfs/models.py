from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PDFDocument(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="pdfs/")
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="pdfs")
    approved = models.BooleanField(default=False)

    def __str__(self):
        return self.title
