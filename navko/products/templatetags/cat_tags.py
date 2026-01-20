from django import template
from products.models import PurposeCat


register = template.Library()

@register.inclusion_tag('products/cat_menu.html')
def cats_menu(cat_active=None):
    categories = PurposeCat.objects.all()

    return {'categories': categories,
            'cat_active': cat_active}
