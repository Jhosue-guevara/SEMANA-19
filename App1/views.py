from django.shortcuts import render,redirect
from .formularios.registerform import NewUserForm
from .formularios.LoginForm import LoginForm
from django.http import HttpResponseRedirect
from .models import Productos,Proveedores
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductosForm


from django.contrib import messages
import sweetify

def reg_user(request):
    if request.method == "POST":
        formulario = NewUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            # Resto del código
            return HttpResponseRedirect("/")  # Redirigir a la página de inicio después del registro
        else:
            sweetify.error(request, 'Por favor, corrija los errores en el formulario.', button='Ok', timer=3000)
    else:
        formulario = NewUserForm()
    return render(request, "Reg_user.html", {"form": formulario})

@login_required(login_url='login')
def index(request):
    es_cajero = request.user.groups.filter(name='Cajero').exists()
    es_estudiante = request.user.groups.filter(name='Estudiante').exists()
    
    if es_cajero:
        # Si el usuario es cajero (que tiene permisos de administrador), se le permite el acceso
        return render(request, 'index.html', {'user': request.user, 'es_cajero': es_cajero, 'es_estudiante': es_estudiante})
    elif es_estudiante:
        # Si el usuario es estudiante (usuario normal), se le permite el acceso
        return render(request, 'index.html', {'user': request.user, 'es_cajero': es_cajero, 'es_estudiante': es_estudiante})
    else:
        # Si el usuario no tiene ninguno de los roles especificados, se le niega el acceso
        return HttpResponseForbidden("No tienes permisos para acceder a esta página.")

def iniciar_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
        



            if user is not None:
                login(request, user)
                return redirect('home')
        else: 
            username = request.POST.get('username')
            password = request.POST.get('password')
            if not username or not password:
                 print("Campos de usuario y contraseña son obligatorios.")
            else:
                print("Datos de usuario o contraseña incorrectos.")
        print(form.errors)
        
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
def cerrar_sesion(request):
    logout(request)
    return redirect('login')
def lista_proveedores(request):
    proveedores = Proveedores.objects.all()
    return render(request, 'lista_proveedores.html', {'proveedores': proveedores})

def agregar_proveedor(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        # Crear el nuevo proveedor
        Proveedores.objects.create(nombre=nombre, telefono=telefono)
        return redirect('lista_proveedores')
    return render(request, 'agregar_proveedor.html')

def editar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedores, pk=proveedor_id)
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')
        # Actualizar el proveedor existente
        proveedor.nombre = nombre
        proveedor.telefono = telefono
        proveedor.save()
        return redirect('lista_proveedores')
    return render(request, 'editar_proveedor.html', {'proveedor': proveedor})

def eliminar_proveedor(request, proveedor_id):
    proveedor = get_object_or_404(Proveedores, pk=proveedor_id)
    if request.method == 'POST':
        proveedor.delete()
        return redirect('lista_proveedores')
    return render(request, 'eliminar_proveedor.html', {'proveedor': proveedor})

def lista_productos(request):
    productos = Productos.objects.all()
    return render(request, 'lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductosForm(request.POST)
        if form.is_valid():
            producto = form.save(commit=False)
            producto.save()
            return redirect('lista_productos')
    else:
        form = ProductosForm()
    return render(request, 'agregar_producto.html', {'form': form})

def editar_producto(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)
    if request.method == 'POST':
        form = ProductosForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('lista_productos')
    else:
        form = ProductosForm(instance=producto)
    return render(request, 'editar_producto.html', {'form': form})

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('lista_productos')
    return render(request, 'eliminar_producto.html', {'producto': producto})



