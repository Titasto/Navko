from django.urls import path
from .views import CartProduct, controller_cart_action

app_name = 'cart'

urlpatterns = [
    path('cart', CartProduct.as_view(), name='carts'),
    path('cart/action/<int:productid>/', controller_cart_action, name='cart_action')
]
