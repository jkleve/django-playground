from django.shortcuts import render
from django.views.generic.base import TemplateView

from .models import Cart, Store, StoreItem


class CartView(TemplateView):
    template_name = 'store/cart_view.html'
    model = Cart


class StoreView(TemplateView):
    template_name = 'store/store.html'
    model = Store
    context_object_name = 'items'
    queryset = StoreItem.objects.all()


class ItemView(TemplateView):
    model = StoreItem
