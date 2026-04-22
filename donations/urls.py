from django.urls import path
from . import views

urlpatterns = [
    path('', views.initiate_donation, name='initiate-donation'),
    path('pay/<int:donation_id>/', views.mock_gateway, name='mock-gateway'),
]
