from django.contrib import admin

from .models import HkCategorias, HkSubcategorias, HkItem

@admin.register(HkCategorias)
class HkCategoriasAdmin(admin.ModelAdmin):
    list_display = ('id','nome')

@admin.register(HkItem)
class HkItemAdmin(admin.ModelAdmin):
    list_display = ('id_categoria','id_subcategoria','titulo','texto')

