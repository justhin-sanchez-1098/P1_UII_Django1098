from django.contrib import admin
from . import views

urlpatterns = [
    path("",views.hola, name="medinaclase_app"),
]
