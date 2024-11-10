# myapp/urls.py (or project/urls.py if you're using project-wide URLs)
from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),  # This is your original 'index' page
    path('', lambda request: redirect('index')),  # Redirect the root path (/) to /index/
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add_student'),
    path('edit/<student_id>/', views.edit_student, name='edit_student'),
    path('delete/<student_id>/', views.delete_student, name='delete_student'),
]
