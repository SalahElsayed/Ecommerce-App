from django.urls import path
from product.views import ProductListView, ProductRetrieveView, CategoryRetrieveView, CategroyListView

urlpatterns = [
    path('list/', ProductListView.as_view(), name='product-list'),
    path('detail/<str:slug>/', ProductRetrieveView.as_view(), name='product-detail'),
    path('category/list/', CategroyListView.as_view(), name='category-list'),
    path('category/detail/<int:pk>/', CategoryRetrieveView.as_view(), name='category-detail'),
]
