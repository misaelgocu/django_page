#buscador/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.buscador_posts, name='buscador_posts'),
]
