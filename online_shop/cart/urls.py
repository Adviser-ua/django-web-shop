# coding: utf-8
# Konstantyn Davidenko

from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.CartDetail, name='CartDetail'),
    url(r'^remove/(?P<product_id>\d+)/$', views.CartRemove, name='CartRemove'),
    url(r'^delete/(?P<product_id>\d+)/$', views.CartDelete, name='CartDelete'),
    url(r'add/(?P<product_id>\d+)/$', views.CartAdd,name="CartAdd"),
]