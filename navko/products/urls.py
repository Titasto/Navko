from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.AllProducts.as_view(), name='products'),
    path('cat/<slug:cat_slug>', views.CatView.as_view(), name='cat'),
    path('add_to_cart/<int:productid>', views.add_cart_button, name='add_to_cart'),
    path('<slug:slug>', views.ProductPage.as_view(), name='product_page'),]