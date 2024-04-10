from django.urls import path
from .views import FileUploadView, SuccessView

urlpatterns = [
    path("", FileUploadView.as_view(), name="upload_file"),
    path("success", SuccessView.as_view(), name="success"),
]