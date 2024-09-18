from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path("login/", views.login_user, name="login_user"),
    path("cadastro/", views.cadastro_cliente, name="cadastro_cliente"),
]
