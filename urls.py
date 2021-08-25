from django.urls import path
from . import views

app_name = 'wbdj'

urlpatterns = [
    path('', views.indexwb, name='indexwb')
]
