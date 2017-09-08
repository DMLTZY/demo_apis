# coding:utf-8
import time
from django.utils import timezone
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class ClientInfo(APIView):
    http_method_names = ['get']

    def get(self, request):
        client_ip = request.META.get('REMOTE_ADDR', '')
        client_host = request.META.get('REMOTE_HOST', '')
        return Response({'ip': client_ip, 'host': client_host},
                        status=status.HTTP_200_OK)

client_info = ClientInfo.as_view()


class Now(APIView):
    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        py_now = time.strftime('%Y-%m-%d %H:%M:%S',
                               time.localtime(time.time()))
        dj_now = timezone.now()
        return Response({'py_now': py_now, 'dj_now': dj_now},
                        status=status.HTTP_200_OK)

get_time = Now.as_view()


class Handle(APIView):
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        pass
