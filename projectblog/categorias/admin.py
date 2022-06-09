from django.contrib import admin
from .models import Categoria


class CatAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_da_categoria')
    list_display_links = ('id', 'nome_da_categoria')


admin.site.register(Categoria, CatAdmin)
