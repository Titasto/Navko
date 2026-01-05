from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.template.context_processors import request
from django.views.generic import ListView
from .models import Cart


# Create your views here.
class CartProduct(ListView):
    template_name = 'cart/all_cart.html'
    extra_context = {'title': 'Cart'}
    context_object_name = 'carts'
    model = Cart

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user_id=self.request.user)
        return cart.item.all()
