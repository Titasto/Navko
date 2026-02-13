import json

from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView, ListView, TemplateView
from .models import Product
from cart.models import Cart, CartItem


# Create your views here.
class ProductPage(DetailView):
    template_name = 'products/product_page.html'
    model = Product
    slug_field = 'slug'
    extra_context = {}
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['price'] = self.object.product_sensitive_info.price
        context['status'] = self.object.product_sensitive_info.status

        return context


class AllProducts(ListView):
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'product'


def add_cart_button(request, productid):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=productid)
        cart, created = Cart.objects.get_or_create(user_id=request.user)

        cart_item, item_created = CartItem.objects.get_or_create(
            cart=cart,
            product=product,
            defaults={'count': 1}
        )

        if not item_created:
            cart_item.count += 1
            cart_item.save()

        return JsonResponse({
            'success': True,
            'count': cart_item.count
        })

    return JsonResponse({'success': False}, status=400)


