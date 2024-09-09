from django.urls import path

from . import views

urlpatterns = [ 
    path("", views.index, name="index"),
    path("<int:id_persona>", views.persona_id, name="detail_persona"),
    path("personas_list", views.personas_list, name="personas_list"),
    path("personas_template", views.personas_template, name="personas_template"),
]