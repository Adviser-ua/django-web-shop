# coding: utf-8
# Konstantyn Davidenko

from django.conf.urls import url
from django.urls import re_path

from . import views

urlpatterns = [
    # url('list/$', views.ProductList, name='ProductList'),
    url('list/$', views.AllProduct.as_view(), name='ProductList'),
    url('(?P<id>\d+)$', views.ProductDetail, name='ProductDetail'),
    re_path(r'list/?', views.Search.as_view(), name='search'),
    url('^$', views.MainPage, name='home'),
]