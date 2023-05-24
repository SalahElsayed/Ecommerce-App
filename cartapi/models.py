from django.db import models
from user.models import CustomUser 
from product.models import Product 
# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1) 

    def __str__(self):
        return f"{self.user.username}'s Cart - {self.product.name}"
    
