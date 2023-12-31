from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    
    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    #correo = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    #tipo_consulta = forms.IntegerField(widget=forms.Select(attrs={"class": "form-control"}))
    #comentario = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control"}))

    
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje"]
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        
        
        
class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2"]