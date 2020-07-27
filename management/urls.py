from django.urls import path, include

from . import views

urlpatterns = [
    path('mintcar/', views.mint_car, name='mint_car'),    
]
