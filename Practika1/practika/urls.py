from django.urls import path
from .views import register, upload_file, upload_success, profile_view

urlpatterns = [
    path('register/', register, name='register'),
    path('upload/', upload_file, name='upload_file'),
    path('upload/success/', upload_success, name='upload_success'),
    path('', register, name='register'),
    path('accounts/profile/', profile_view, name='profile'),
    path('accounts/profile/', profile_view, name='profile_view'),
    path('accounts/upload/', upload_file, name='upload_file'),
    path('accounts/upload/success/', upload_success, name='upload_success'),
]
