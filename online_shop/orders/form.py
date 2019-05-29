# coding: utf-8
# Konstantyn Davidenko
from django import forms

from orders.models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'contact_number', 'email', 'address', 'city']
