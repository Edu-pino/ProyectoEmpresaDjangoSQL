from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, get_user, logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse


# Create your views here.

def loginView(request): 
    if request.method == 'GET':# Comprueba si el request es un GET
        return render(request, "login.html") # Renderiza y retorna la página de login
    else:  # Si el metodo no es GET, lo asumirá como POST
        print(request.POST.get('username'));
        print(request.POST.get('password'));
        
        user= authenticate(request,
                           username= request.POST.get('username'),
                           password= request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('landingView')
        else:
            return HttpResponse("Validación incorrecta")

@login_required
def landingView(request):
    if request.method == 'GET':
        return render(request, "landing.html")

def logoutView(request):
    logout(request)
    return redirect('/')

def get_data(request):
    from app_sage.connection_query.connection import Connection 
    if request.method =='GET':
        # Suponiendo que quieres recoger todos los objetos de un modelo
        filas_datos, nombres_columnas = Connection.conexion(request)
        
        print(filas_datos)
        print(nombres_columnas)
    
        if not filas_datos: # Comprueba si la consulta esta bien hecha
            print("Hubo un error en la consulta")
            return JsonResponse({})
        
        elif len(filas_datos)<1: # Comprueba si hay datos en la consulta
            print("No se encontraron datos en la consulta")
            return JsonResponse({'state':'empty', 'data': []})
        
        else:
            data = {
            "titulos": nombres_columnas,
            "filas": filas_datos
        }
            print("hola")
            print(data)
            print("adios")
            
            return JsonResponse(data, safe=False)    
    else:
        # Renderiza la página inicialmente sin datos
        return render(request, 'app_sage/landing.html')
    

    
def extraercodigocliente(request):
    from app_sage.models import Extrafields
    # Obtener el modelo de usuario personalizado
    User = get_user_model()
    
    # Obtener el usuario asociado a la solicitud
    usuario = User.objects.get(username=request.user.username)
    # Obtener los campos extra asociados al usuario
    data = Extrafields.objects.filter(user = usuario)
    
    # Suponiendo que CodCliente es un campo en el modelo Extrafields, puedes obtener su valor así
    cod = None
    if data.exists():
        cod = data.first().CodCliente
    # Ahora puedes hacer lo que necesites con el CodCliente 
    return cod
