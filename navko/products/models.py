from django.db import models
from datetime import date

from django.urls import reverse
from django.utils.text import slugify


class Product(models.Model):
    name = models.CharField(null=False, max_length=255)
    #photo = models.ImageField()
    slug = models.SlugField(max_length=255, unique=True)
    description = models.CharField(blank=True, max_length=255)
    brand = models.CharField(blank=True, max_length=255)
    series = models.CharField(blank=True, max_length=255)
    release_year = models.DateTimeField(blank=True, default=date.today)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_page', kwargs={'slug': self.slug})


class ProductSensitive(models.Model):
    product_id = models.OneToOneField(Product, on_delete=models.CASCADE,
                                   related_name='product_sensitive_info')

    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.BooleanField(blank=False)
