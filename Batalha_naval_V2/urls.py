
from django.contrib import admin
from django.urls import path
from app_batalha_naval_V2 import views

urlpatterns = [
    # rota, view responsavel, nome de referencia
    # https://iagomunoz.github.io/Batalha_naval_V2
    path('/login', views.home, name = 'login')
]
