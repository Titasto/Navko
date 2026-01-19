import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import DetailView, ListView
from .models import Product
from cart.models import Cart, CartItem
from .models import PurposeCat


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
    context_object_name = 'products'


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

#Add function to check self.category exist
class CatView(ListView):
    template_name = 'products/products.html'
    model = Product
    context_object_name = 'products'


    def get_queryset(self):
        self.category = get_object_or_404(PurposeCat, slug=self.kwargs['cat_slug'])
        return self.category.products.all().distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.category.name
        context['cat_active'] = self.category
        return context


