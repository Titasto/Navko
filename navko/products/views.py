from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import DetailView, ListView
from django.views.generic.edit import FormMixin

from .models import Product
from cart.models import Cart, CartItem
from .models import PurposeCat
from reviews.forms import ReviewForm


class ProductPage(FormMixin, DetailView):
    template_name = 'products/product_page.html'
    context_object_name = 'product'

    model = Product
    form_class = ReviewForm

    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['form'] = self.get_form()
        context['reviews'] = self.object.reviews.filter(is_published=True).select_related("user_id")
        context['price'] = self.object.product_sensitive_info.price
        context['status'] = self.object.product_sensitive_info.status

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        review = form.save(commit=False)
        review.product_id = self.object
        review.user_id = self.request.user
        review.save()

        return self.get_success_url()

    def get_success_url(self):
        return redirect(self.object.get_absolute_url())


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
