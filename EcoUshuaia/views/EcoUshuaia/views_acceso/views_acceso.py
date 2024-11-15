from django.shortcuts import render
from django.views.generic import TemplateView


class Acceso(TemplateView):
    template_name = 'EcoUshuaia/acceso/acceso.html'
