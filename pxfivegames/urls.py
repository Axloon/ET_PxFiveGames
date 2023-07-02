from django.urls import path
from .views import home, galeria, nosotros ,contacto, agregar_producto, listar_producto, registro

urlpatterns = [
    path('', home, name="home"),
    path('galeria/', galeria, name="galeria"),
    path('nosotros/', nosotros, name="nosotros"),
    path('contacto/', contacto, name="contacto"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-producto/', listar_producto, name="listar_producto"),
    path('registro/', registro, name="registro"),
]