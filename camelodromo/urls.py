from django.urls import path
from .views import cadastrar_usuario

urlpatterns = [
    path('cadastro/', cadastrar_produto, name='cadastrar_produto'),
    path('', listar_produtos, name='listar_produtos'),
]
urlpatterns = [
    path('cadastro/', cadastrar_usuario, name='cadastro'),
]