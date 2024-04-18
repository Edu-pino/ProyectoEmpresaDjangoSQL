from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, get_user, logout,get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
import json


# Create your views here.

def loginView(request): 
    if request.method == 'GET':# Comprueba si el request es un GET
        return render(request, "login.html") # Renderiza y retorna la página de login
    else:  # Si el metodo no es GET, lo asumirá como POST       
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

def check_data(filas_datos, nombres_columnas):
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
        return JsonResponse(data, safe=False)    

def get_data(request):
    from app_sage.connection_query.connection import Connection
    if request.method =='GET':
        # Suponiendo que quieres recoger todos los objetos de un modelo
        filas_datos, nombres_columnas = Connection.consulta_1(request)
        
        return check_data(filas_datos, nombres_columnas)

    else:
        # Renderiza la página inicialmente sin datos
        return render(request, 'app_sage/landing.html')
    
def get_data_consulta_articulos_precio(request):
    from app_sage.connection_query.connection import Connection 
    if request.method =='GET':
        # Suponiendo que quieres recoger todos los objetos de un modelo
        filas_datos, nombres_columnas = Connection.consulta_articulos_precio(request)
                
        return check_data(filas_datos, nombres_columnas)
   
    else:
        # Renderiza la página inicialmente sin datos
        return render(request, 'app_sage/landing.html')
    
def get_data_consulta_articulos(request):
    from app_sage.connection_query.connection import Connection 
    if request.method =='GET':
        # Suponiendo que quieres recoger todos los objetos de un modelo
        filas_datos, nombres_columnas = Connection.consulta_articulos(request)
        
        return check_data(filas_datos,nombres_columnas)   
    else:
        # Renderiza la página inicialmente sin datos
        return render(request, 'app_sage/landing.html')
    
def get_data_consulta_albaran(request):
    from app_sage.connection_query.connection import Connection 
    if request.method =='GET':
        # Suponiendo que quieres recoger todos los objetos de un modelo
        filas_datos, nombres_columnas = Connection.consulta_albaran(request)
        
        return check_data(filas_datos,nombres_columnas)   
    else:
        # Renderiza la página inicialmente sin datos
        return render(request, 'app_sage/landing.html')
    
def get_data_consulta_cabecera_albaran(request):
    from app_sage.connection_query.connection import Connection 
    if request.method =='GET':
        # Suponiendo que quieres recoger todos los objetos de un modelo
        filas_datos, nombres_columnas = Connection.consulta_cabecera_albaran(request)
        
        return check_data(filas_datos,nombres_columnas)   
    else:
        # Renderiza la página inicialmente sin datos
        return render(request, 'app_sage/landing.html')
    
def get_data_oferta_cliente(request):
    from app_sage.connection_query.connection import Connection 
    if request.method =='GET':
        # Suponiendo que quieres recoger todos los objetos de un modelo
        filas_datos, nombres_columnas = Connection.OfertaCliente(request)
        
        return check_data(filas_datos,nombres_columnas)   
    else:
        # Renderiza la página inicialmente sin datos
        return render(request, 'app_sage/landing.html')
    
    
    
    
def get_data_modal(request):
    from app_sage.connection_query.connection import Connection
    try:
        filas_datos, columna = Connection.table_modal(request)
        print("He salido de la consulta")
        return JsonResponse({
            'status': 'success',
            'rows': filas_datos,
            'columns': columna
        })
    except Exception as e:
        print("Ocurrió un error al obtener los datos del modal:", str(e))
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)


    
    

    
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


def manejar_datos_celda(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            cell_data = data.get('cellData')
            column_name = data.get('columnName')
            return {'cellData': cell_data, 'columnName': column_name}
        except json.JSONDecodeError:
            return {'error': "JSON inválido"}
    return {'error': "Método no POST"}



def get_data_frontend(request):
    data = json.loads(request.body.decode('utf-8'))  # Decodifica y carga los datos JSON
    listaValores = list(data.values())
    print('Datos recibidos:', listaValores)
    return listaValores

