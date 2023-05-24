
from rest_framework import generics
from .models import CartItem
from .serializers import CartItemSerializer


# Cart items List API View 
class CartItemListAPIView(generics.ListCreateAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)

# Cart Item Detail, Update, Destroy View 
class CartItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        user = self.request.user
        return CartItem.objects.filter(user=user)
