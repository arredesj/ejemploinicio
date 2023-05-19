
from django. shortcuts import render,HttpResponse
def saludar(request):
    return HttpResponse("hola")
# Create your views here.
def saludar_con_nombre(request,nombre):
    return HttpResponse(f"Hola {nombre}")
