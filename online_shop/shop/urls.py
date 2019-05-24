# coding: utf-8
# Konstantyn Davidenko

from django.conf.urls import url
from . import views

urlpatterns = [
    url('list/$', views.ProductList, name='ProductList'),
    url('(?P<id>\d+)$', views.ProductDetail, name='ProductDetail'),
    url('^$', views.MainPage, name='home'),
]