from django.urls import path
from . import views

app_name = 'appMono'

urlpatterns = [
    path('', views.index, name = 'index'),
]