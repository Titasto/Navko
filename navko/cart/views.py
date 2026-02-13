from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request
from django.views.generic import ListView

from products.models import Product
from .models import Cart, CartItem
import json

from django.http import JsonResponse

# Create your views here.
class CartProduct(ListView):
    template_name = 'cart/all_cart.html'
    extra_context = {'title': 'Cart'}
    context_object_name = 'carts'
    model = Cart

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user_id=self.request.user)
        return cart.item.all()


def controller_cart_action(request, productid):
    if request.method == 'POST':
        print('Maybe')
        product = get_object_or_404(Product, id=productid)
        cart = get_object_or_404(Cart, user_id=request.user)
        cart_item = get_object_or_404(CartItem, cart=cart, product=product)

        data = json.loads(request.body)
        action = data.get('action')

        match action:
            case 'increase':
                cart_item.count += 1
                print('+')
                cart_item.save()
            case 'downgrade':
                cart_item.count -= 1
                print('-')
                cart_item.save()
            case 'delete':
                cart_item.count = 0
                print('&')
                cart_item.save()

        return JsonResponse({
            'success': True,
            'count': cart_item.count
        })
    return JsonResponse({'success': False}, status=400)
