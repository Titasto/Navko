from django.conf import settings
from django.db import models
from products.models import Product


class Cart(models.Model):
    # delete id from end
    user_id = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_cart')


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart')
    count = models.IntegerField(blank=False)

