from django.urls import path
from .views import *

app_name = "pokemon"

urlpatterns = [
    path('get', get_pokemon, name='get'),
    path('create', create_pokemon, name='create'),
]
