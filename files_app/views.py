import os
from django.shortcuts import render, redirect
from django.views import View
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseBadRequest
from cryptography.fernet import Fernet
from .models import EncryptedFile
from fileUploader.settings import BASE_DIR


class FileUploadView(View):
    template_name = "files_app/upload.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):

        if request.method == "POST" and request.FILES['myfile']:

            myfile = request.FILES['myfile']
            encrypted_file = EncryptedFile.objects.create(
                uploaded_file=myfile
            )

            # Key for encryption
            key = Fernet.generate_key()
            fernet = Fernet(key)

            # encrypting file
            file_content = encrypted_file.uploaded_file.read()
            encrypted_content = fernet.encrypt(file_content)

            # checking if encrypted folder exists
            if not os.path.exists(f"{BASE_DIR}/media/encrypted"):
                os.makedirs(f"{BASE_DIR}/media/encrypted")

            # saving encrypted file
            with open(f'{BASE_DIR}/media/encrypted/{myfile.name}.encrypted', "wb") as file:
                file.write(encrypted_content)

            # saving date in db
            encrypted_file.encrypted_file_key = key.decode()
            encrypted_file.encrypted_file_url = f"encrypted/{myfile.name}.encrypted"
            encrypted_file.save()

            request.session['key'] = str(key)
            request.session['url'] = encrypted_file.encrypted_file_url

            return redirect('success')

class SuccessView(View):

    template_file = "files_app/success.html"

    def get(self, request):

        if request.session.get('key') is None or request.session.get('url') is None:
            return HttpResponseBadRequest()

        key = request.session.get('key')
        url = request.session.get('url')

        del request.session['key']
        del request.session['url']

        return render(request, self.template_file, {'key': str(key), 'url': url})
