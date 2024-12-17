from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_produtos, name='listar-produtos'),
    path('estoque/cadastrar', views.cadastrar_produto, name='cadastrar-produto'),
    path('estoque/editar<int:pk>', views.editar_produto, name="editar-produto"),
    path('estoque/excluir<int:pk>', views.excluir_produto, name='excluir-produto'),
    path('produto/<int:pk>/', views.visualizar_produto, name='visualizar-produto'),
]
