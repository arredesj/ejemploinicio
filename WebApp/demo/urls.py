
from django.urls import path
from .views import saludar,saludar_con_nombre

urlpatterns=[
   path("saludar/", saludar, name="saludar"),
   path("saludar_con_nombre/<str:nombre>",saludar_con_nombre,name="saludar_con_nombre"),

]