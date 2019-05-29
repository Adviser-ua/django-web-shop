from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from online_shop import settings
from orders.models import Order
from .liqpay import LiqPay


class PayView(TemplateView):
    template_name = 'payment.html'

    def get(self, request, *args, **kwargs):
        order_id = request.session.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        cost = order.get_total_cost()
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        params = {
            'action': 'pay',
            'amount': str(cost),
            'currency': 'UAH',
            'description': 'Оплата заказа №' + str(order_id),
            'order_id': order_id,
            'version': '3',
            'sandbox': 1,  # sandbox mode, set to 1 to enable it
        }
        signature = liqpay.cnb_signature(params)
        data = liqpay.cnb_data(params)
        return render(request, self.template_name, {'signature': signature, 'data': data})


@method_decorator(csrf_exempt, name='dispatch')
class PayCallbackView(View):
    def post(self, request, *args, **kwargs):
        liqpay = LiqPay(settings.LIQPAY_PUBLIC_KEY, settings.LIQPAY_PRIVATE_KEY)
        data = request.POST.get('data')
        signature = request.POST.get('signature')
        sign = liqpay.str_to_sign(settings.LIQPAY_PRIVATE_KEY + data + settings.LIQPAY_PRIVATE_KEY)
        if sign == signature:
            print('callback is valid')
        response = liqpay.decode_data_from_str(data)
        print('callback data', response)
        return HttpResponse()


