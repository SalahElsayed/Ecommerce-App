from rest_framework import serializers 
from product.models import Product, Category 


# Product Serializer 
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product 
        fields = '__all__'


# Category Serializer 
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ('name', 'description', )