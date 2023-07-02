from django.contrib import admin
from .models import Categoria, Producto, Contacto
# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "disponible", "precio", "categoria"]
    list_editable = ["precio"]
    search_fields = ["nombre"]
    list_filter = ["categoria", "disponible"]
    list_per_page = 5

admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Contacto)