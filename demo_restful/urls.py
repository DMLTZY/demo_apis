# coding:utf-8
from django.conf.urls import url
from . import apis


# http://127.0.0.1:8002/apis/...
urlpatterns = [
    url(r'^users/$', apis.user_list, name='user_list'),
    url(r'^users/create/$', apis.user_create, name='user_create'),
    url(r'^users/(?P<username>\w+)/$', apis.user_detail, name='user_detail'),
    url(r'^users/(?P<pk>\d+)/edit/$', apis.user_update, name='user_update'),
    url(r'^users/(?P<pk>\d+)/delete/$', apis.user_delete, name='user_delete'),
    url(r'^gt/$', apis.get_time, name='get_time'),
    url(r'^ci/$', apis.client_info, name='client_info'),
    url(r'^ep/$', apis.echo_post, name='echo_post'),
    url(r'^sleep/$', apis.do_celery, name='do_celery'),
]
