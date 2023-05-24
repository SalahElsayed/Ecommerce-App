from django.urls import path
from .views import  CartItemListAPIView, CartItemDetailAPIView

urlpatterns = [
    path('items/', CartItemListAPIView.as_view(), name='cart-list'),
    path('items/<int:pk>/', CartItemDetailAPIView.as_view(), name='cart-detail'),
]
