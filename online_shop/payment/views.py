from django.shortcuts import render

from django.urls import reverse
from django.shortcuts import render
from paypal.standard.forms import PayPalPaymentsForm

from django.shortcuts import render, get_object_or_404
from decimal import Decimal
from django.conf import settings

from paypal.standard.forms import PayPalPaymentsForm
from online_shop.orders.models import Order
from django.views.decorators.csrf import csrf_exempt


def view_that_asks_for_money(request):

    # What you want the button to do.
    paypal_dict = {
        "business": "receiver_email@example.com",
        "amount": "10000000.00",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('your-return-view')),
        "cancel_return": request.build_absolute_uri(reverse('your-cancel-view')),
        "custom": "premium_plan",  # Custom command to correlate to some function later (optional)
    }

    # Create the instance.
    form = PayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "payment.html", context)


# Create your views here.
def PaymentProcess(request):
    order_id = request.session.get('order_id')
    order = get_object_or_404(Order, id=order_id)
    host = request.get_host()

    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': '%.2f' % order.get_total_cost().quantize(Decimal('.01')),
        'item_name': 'Заказ {}'.format(order.id),
        'invoice': str(order.id),
        'currency_code': 'RUB',
        'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
        'return_url': 'http://{}{}'.format(host, reverse('payment:done')),
        'cancel_return': 'http://{}{}'.format(host, reverse('payment:canceled'))
    }

    form = PayPalPaymentsForm(initial=paypal_dict)
    return render(request, 'payment/process.html',{'order':order, 'form':form})


@csrf_exempt
def PaymentDone(request):
    return render(request, 'payment/done.html')


@csrf_exempt
def PaymentCanceled(request):
    return render(request, 'payment/canceled.html')
