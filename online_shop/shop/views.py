from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response
from .models import Product


# Страница с товарами
def ProductList(request, category_slug=None):
    # category = None
    # # categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/product/list.html', {
        'products': products
    })


# Страница товара
def ProductDetail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    # cart_product_form = CartAddProductForm()
    # return render(request, 'shop/product/detail.html',{'product': product,'cart_product_form': cart_product_form})
    return render(request, 'shop/product/detail.html', {'product': product})