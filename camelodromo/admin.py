from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')  # campos mostrados na lista do admin
    search_fields = ('nome',)
