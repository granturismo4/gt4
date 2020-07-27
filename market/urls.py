from django.urls import path

from . import views

urlpatterns = [
    path('', views.market_index, name='market_index'),
    path('cardetail/<int:id>/', views.market_cardetail, name='market_cardetail'),
    path('set_wallet_session/<str:wallet_address>/', views.set_wallet_session, name='set_wallet_session'),
    path('make_transfer/', views.make_transfer, name='make_transfer'),
]
