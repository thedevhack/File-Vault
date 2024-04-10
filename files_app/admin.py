from django.contrib import admin
from .models import EncryptedFile

class EncryptedFileContents(admin.ModelAdmin):

    list_display = ("uid", "encrypted_file_url")

admin.site.register(EncryptedFile, EncryptedFileContents)
