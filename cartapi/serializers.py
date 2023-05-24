from rest_framework import serializers
from cartapi.models import CartItem
from product.serializers import ProductSerializer 

class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = CartItem
        fields = '__all__' 
        
