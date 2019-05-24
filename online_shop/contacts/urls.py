# coding: utf-8
# Konstantyn Davidenko


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^contacts$', views.ContactsView, name='contacts'),
    url(r'^pay_ship$', views.PayShipment, name='pay_ship'),
]