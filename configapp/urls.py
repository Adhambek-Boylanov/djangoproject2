from django.urls import path
from .views import *


urlpatterns = [
    path('', info, name='dashboard'),
    path('add_car/', add_car, name='add_car'),
    path('add_brand/' ,add_brand, name='add_brand'),
    path('add_salon/' ,add_salon, name='add_salon'),
    path('salon_car/<int:brand_pk>/<int:salon_pk>/',salon_car, name='salon_car'),
    path('detail_salon/<int:pk>/',detail_salon, name='detail_salon'),

    ]