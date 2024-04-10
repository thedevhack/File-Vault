from django.db import models
from uuid import uuid4

class EncryptedFile(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    uploaded_file = models.FileField(upload_to='uploads/')
    encrypted_file_key = models.CharField(max_length=255)
    encrypted_file_url = models.URLField(blank=True)
