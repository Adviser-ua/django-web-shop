from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, render_to_response

from cart.cart import Cart
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.list import MultipleObjectMixin, ListView

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


class AllProduct(TemplateView):
    template_name = 'shop/product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()
        paginator = Paginator(products, 6)  # Show 25 contacts per page
        page = self.request.GET.get('page')
        page_products = paginator.get_page(page)
        context['products'] = page_products
        return context


class Search(TemplateView):
    template_name = 'shop/product/list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get('name')
        products = Product.objects.filter(name__contains=name)
        paginator = Paginator(products, 6)  # Show 25 contacts per page
        page = self.request.GET.get('page')
        page_products = paginator.get_page(page)
        context['products'] = page_products
        context['queries'] = products
        return context


from django import template
register = template.Library()


@register.simple_tag(takes_context=True)
def url_replace(context, **kwargs):
    query = context['request'].GET.copy()
    query.update(kwargs)
    return query.urlencode()
