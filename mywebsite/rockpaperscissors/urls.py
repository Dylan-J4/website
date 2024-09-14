from django.urls import path
from . import views

urlpatterns = [
    path('', views.rps_home, name='rps_home'),
]