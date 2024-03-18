# main/urls.py

from django.contrib import admin
from django.urls import path
from core.views import upload_image

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/upload_image/', upload_image, name='upload_image'),
    # Add other custom URL patterns as needed
]
