from django.shortcuts import redirect, render, get_object_or_404
from .models import Producto
from .forms import ContactoForm, ProductoForm ,CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.

def home(request):
    return render(request, 'pxfivegames/home.html',)

def galeria(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    
    return render(request, 'pxfivegames/galeria.html', data)

def nosotros(request):
    return render(request, 'pxfivegames/nosotros.html')

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else:
            data["form"] = formulario
            
    return render(request, 'pxfivegames/contacto.html', data)

def agregar_producto(request):
    
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "guardado correctamente"
        else:
            data["form"] = formulario
    
    return render(request, 'pxfivegames/producto/agregar.html', data)

def listar_productos(request):
    productos = Producto.objects.all()
    
    data = {
        'productos': productos
    }
    
    return render(request, 'pxfivegames/producto/listar.html', data)

def modificar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data = {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="listar_productos")
        data["form"] = formulario
    
    return render(request, 'pxfivegames/producto/modificar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="listar_productos")

def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to="home")
        data["form"] = formulario
    
    return render(request, 'registration/registro.html', data)