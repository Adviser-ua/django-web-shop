from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response

from cart.cart import Cart
from .models import Product


# Страница с товарами
def MainPage(request):
    cart = Cart(request)
    return render(request, 'shop/index.html', {'cartItems': cart})


def ProductList(request):
    products = Product.objects.all()
    cart = Cart(request)
    return render(request, 'shop/product/list.html', {
        'products': products, 'cartItems': cart})


# Страница товара
def ProductDetail(request, id):
    product = get_object_or_404(Product, id=id)
    # cart_product_form = CartAddProductForm()
    # return render(request, 'shop/product/detail.html',{'product': product,'cart_product_form': cart_product_form})
    return render(request, 'shop/product/detail.html', {'product': product})
