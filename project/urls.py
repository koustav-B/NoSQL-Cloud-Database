# project/urls.py (replace 'project' with the actual project name)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin URL
    path('', include('testproj.urls')),  # Include the app's URLs (e.g., 'myapp')
]
