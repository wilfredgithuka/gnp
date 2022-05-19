from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='main-dash'),
    path('canbus', views.canbus, name='main-dash')
]
