from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.leaderboard_index, name='leaderboard_index'),    
]
