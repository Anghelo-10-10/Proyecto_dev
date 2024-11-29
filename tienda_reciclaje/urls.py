from django.urls import path
from . import views

urlpatterns = [
    # Página principal
    path('', views.inicio, name='inicio'),

    # Rutas para la gestión de productos
    path('productos/', views.lista_productos, name='lista_productos'),  # Lista de productos
    path('productos/registrar/', views.registrar_producto, name='registrar_producto'),  # Registrar producto

    # Rutas para los puntos de reciclaje
    path('puntos-reciclaje/', views.lista_puntos_reciclaje, name='lista_puntos_reciclaje'),  # Lista de puntos de reciclaje
    path('puntos-reciclaje/registrar/', views.registrar_reciclaje, name='registrar_reciclaje'),  # Registrar reciclaje
]
