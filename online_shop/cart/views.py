# Create your views here.

from django.shortcuts import render, redirect, get_object_or_404
from shop.models import Product
from .cart import Cart


def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product)
    return redirect('cart:CartDetail')


def CartDelete(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.delete(product)
    return redirect('cart:CartDetail')


def CartRemove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:CartDetail')


def CartDetail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})
