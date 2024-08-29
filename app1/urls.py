from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_cartao, name="listar_cartao"),
    path('novo_cliente/', views.novo_cliente, name="novo_cliente"),
    path('formulario/', views.formulario, name="formulario"),
    path('cartao/', views.cartao, name="cartao"),
    path('formulario_post/', views.formulario_post, name="formulario_post"),
    path('cartao_post/', views.cartao_post, name="cartao_post"),
]
