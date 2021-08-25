from django.urls import path
from . import views

app_name = 'mljy'

urlpatterns = [
    path('', views.indexml, name='indexml')
]