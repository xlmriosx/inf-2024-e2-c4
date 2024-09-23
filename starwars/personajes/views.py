from django.shortcuts import render
# Importo estos tres modulos
from .models import Personaje
from django.http import HttpResponse
from django.template import loader

from .forms import PersonajeForm

from django.shortcuts import redirect, get_object_or_404

# Create your views here.
def personajes(request):
    personajes_list = Personaje.objects.all()
    template = loader.get_template("personjes.html")
    context = { "personajes_list": personajes_list}
    return HttpResponse(template.render(context, request))

def personaje_form(request):
    context = { 'form': PersonajeForm() }
    if request.method == "POST":
        form = PersonajeForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save() 
            context["mensaje"] = "Se guardo el form"
            return redirect("pj:personajes")
        else:
            context["mensaje"] = "No se guardo el form"
            context["form"] = form
    
    return render(request, "carga_persona.html", context)

def personaje_delete(request, id):
    personaje = get_object_or_404(Personaje, id=id)
    if request.method == "POST":
        personaje.delete()
        return redirect("pj:personajes")
    return render(request, "personaje_delete.html", {'personaje': personaje})
    