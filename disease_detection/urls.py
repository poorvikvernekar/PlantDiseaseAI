from django.urls import path
from . import views

urlpatterns = [
    path("", views.upload_image, name="upload"),
    path("download-report/", views.download_report, name="download_report"),
]