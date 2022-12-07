from django.urls import path
from .views import *

app_name = "auth"

urlpatterns = [
    path('register', django_register, name='register'),
    path('login', django_login, name='login'),
]
