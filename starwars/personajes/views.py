from django.shortcuts import render
# Importo estos tres modulos
from .models import Personaje
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def personajes(request):
    personajes_list = Personaje.objects.all()
    template = loader.get_template("personjes.html")
    context = { "personajes_list": personajes_list}
    return HttpResponse(template.render(context, request))
