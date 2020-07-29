from django.urls import path

from . import views

urlpatterns = [
    path('<str:wallet>/', views.garage_index, name='garage_index'),
    path('garage_sell/<int:car_id>', views.garage_sell, name='garage_sell'),
    path('upgrade_car/<int:np>/<int:car_id>', views.upgrade_car, name='upgrade_car'),
]
