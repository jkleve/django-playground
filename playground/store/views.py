from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView

from .models import Cart, Store, StoreItem


class CartView(TemplateView):
    template_name = 'store/cart_view.html'
    model = Cart


class StoreView(ListView):
    template_name = 'store/store.html'
    model = StoreItem
    context_object_name = 'items'
    queryset = StoreItem.objects.all()


class ItemView(TemplateView):
    model = StoreItem
