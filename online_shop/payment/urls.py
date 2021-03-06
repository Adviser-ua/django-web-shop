# coding: utf-8
# Konstantyn Davidenko

from django.conf.urls import url

from payment.views import PayView, PayCallbackView


urlpatterns = [
    url(r'^pay/$', PayView.as_view(), name='pay_view'),
    url(r'^pay-callback/$', PayCallbackView.as_view(), name='pay_callback'),
]
