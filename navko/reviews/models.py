from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from products.models import Product


class Reviews(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_review')
    rating = models.IntegerField(null=True)
    text = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)