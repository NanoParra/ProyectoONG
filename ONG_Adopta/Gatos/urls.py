#from django.cof.urls import url
from django.urls import path
from . import views


urlspatterns =[
    path('index', views.index, name='index'), #index es el nombre de la funcion que se tiene que crear
]
