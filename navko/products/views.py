from django.shortcuts import render
from django.views.generic import DetailView, ListView, TemplateView
from .models import Product

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
