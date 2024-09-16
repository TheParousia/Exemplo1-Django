from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.listar_cartao, name="listar_cartao"),
    path('formulario_post/', views.formulario_post, name="formulario_post"),
    path('deletar/<int:id>', views.deletar_cartao, name="deletar_cartao"),
    path('atualizar/<int:id>', views.atualizar_cartao, name="atualizar_cartao"),

    path('novo_cliente/', views.novo_cliente, name="novo_cliente"),
    path('formulario/', views.formulario, name="formulario"),
    path('cartao/', views.cartao, name="cartao"),
    path('cartao_post/', views.cartao_post, name="cartao_post"),
    path('accounts/', include('django.contrib.auth.urls')),
]
