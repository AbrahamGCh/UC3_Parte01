from django.shortcuts import render, HttpResponse

# Create your views here.
def inicio(request):
    mensaje = """ <h1> Bienvenido a LP3 - GARCIA </h1>"""
    return HttpResponse(mensaje)