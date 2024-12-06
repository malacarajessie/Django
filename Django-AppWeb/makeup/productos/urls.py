from django.urls import path
"""from django.shortcuts import redirect"""
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='productos/login.html'), name='login'),
    path('inicio/', views.inicio, name='inicio'),
    path('rimel/', views.rimel, name='hola'),
    path('agrega_producto/', views.agregar_producto, name='agregar'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('agregar_producto/', views.agregar_producto, name='agregar_producto'), 
]
