
from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('',index,name='IND'),
    path('galeria/',galeria,name='GALE'),
    path('quienes/',quienes,name='QUIEN'),
    path('formulario/',formulario,name='FORMU'),
    path('admin_mascota/',admin_mascota,name='ADMIN_MAS'),
    path('ficha_mas/<id>/',ficha_mascota,name='FICHA_MASCOTA'),
    path('buscar_nombre/',buscar_nombre,name='BUSCAR_NOMBRE'),
    path('buscar_descripcion/',buscar_descripcion,name='BUSCAR_DESCRIPCION'),
    path('buscar_categoria/<id>/',buscar_categoria,name='BUSCAR_CAT'),
]
