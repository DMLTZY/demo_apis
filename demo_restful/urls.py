# coding:utf-8
from django.conf.urls import url
from . import apis


urlpatterns = [
    url(r'gt', apis.get_time, name='get_time'),
    url(r'ci', apis.client_info, name='client_info'),
]
