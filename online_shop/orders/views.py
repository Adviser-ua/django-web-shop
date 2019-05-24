from django.shortcuts import render

# Create your views here.
from orders.models import OrderItem

from cart.cart import Cart


def OrderCreate(request):
    cart = Cart(request)
    # if request.method == 'POST':
    #     form = OrderCreateForm(request.POST)
    #     if form.is_valid():
    #         order = form.save(commit=False)
    #         if cart.cupon:
    #             order.cupon = cart.cupon
    #             order.discount = cart.cupon.discount
    #         order.save()
    #         for item in cart:
    #             OrderItem.objects.create(order=order, product=item['product'],
    #                                      price=item['price'],
    #                                      quantity=item['quantity'])
    #         cart.clear()
    #
    #         # Асинхронная отправка сообщения
    #         OrderCreated.delay(order.id)
    #         request.session['order_id'] = order.id
    #         return redirect(reverse('payment:process'))

    # form = OrderCreateForm()
    return render(request, 'orders/order/create.html', {'cart': cart, 'form': form})
