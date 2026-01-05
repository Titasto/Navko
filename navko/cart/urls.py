from django.urls import path
from .views import CartProduct

app_name = 'cart'

urlpatterns = [
    path('cart', CartProduct.as_view(), name='carts')
]
