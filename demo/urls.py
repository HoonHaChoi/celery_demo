from django.urls import path
from . import views

urlpatterns = [
    path('', views.app_core, name='main'),
]
