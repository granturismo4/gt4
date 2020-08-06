from django.urls import path

from . import views

urlpatterns = [
    path('<str:wallet>/', views.playerprofile_index, name='playerprofile_index'),
]
