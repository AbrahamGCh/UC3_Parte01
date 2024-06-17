from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def inicio(request):
    mensaje = """ <h1> Bienvenido a LP3 - GARCIA </h1>"""
    return HttpResponse(mensaje)


def rango(request):
    a = 10
    b = 20
    resultado = f"""
        <h2> Numeros de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """   
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(resultado)


def rango2(request,a,b):
    if a>b:
        return redirect('rango2',a=b, b=a)
    
    resultado = f"""
        <h2> Números de [{a},{b}] </h2>
        Resultado: <br>
        <ul> 
    """
    
    while a<=b:
        resultado +=  f"<li> {a} </li>"
        a+=1
    resultado += "</ul"
    return HttpResponse(resultado)


def examen(request):
    mensaje = """ <h1> Nombre del Estudiante 01  : GARCIA </h1>
    
    <h1>  Git Hub:  https://github.com/AbrahamGCh/UC3_Parte01.git </h1> """
    return HttpResponse(mensaje)
