from django.urls import path
from .views import *


urlpatterns = [
    path('', info, name='dashboard'),
    path('add_car/', add_car, name='add_car'),
    path('add_brand/' ,add_brand, name='add_brand'),
    path('add_salon/' ,add_salon, name='add_salon'),
    path('brand/<int:pk>/<int:pk1>/',brand, name='brand'),

    ]