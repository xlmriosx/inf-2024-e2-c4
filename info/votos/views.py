from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
# GET
# POST
# DELETE
# PUT
def index(request):
    return HttpResponse("Hola mundo desde la web!")
