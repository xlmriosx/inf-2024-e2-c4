from django.urls import path
from .views import personaje_form, personajes, personaje_delete

app_name = 'pj'

urlpatterns = [
    path('', personajes, name="personajes"),
    path('carga_personaje/', personaje_form, name="carga_personaje"),
    path('personaje/delete/<int:id>', personaje_delete, name="personaje_delete"),
]

