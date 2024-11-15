from django.urls import path
from EcoUshuaia.views import *

app_name = 'EcoUshuaia'
urlpatterns = [
    path('acceso/', Acceso.as_view(), name='acceso')
]
