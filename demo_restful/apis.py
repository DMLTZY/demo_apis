# coding:utf-8
import time
from django.utils import timezone
from rest_framework import status
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView,
                                     CreateAPIView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import (IsAuthenticated, IsAdminUser,
                                        )
from user.models import User
from .serializers import (UserSerializer, UserDetailSerializer,
                          UserCreateUpdateSerializer)
from .permissions import IsAdminOrOwner, ReadOnly, IsSuperuser


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


class UserListAPIView(ListAPIView):

    permission_classes = [IsAdminUser]
    queryset = User.objects.all()
    serializer_class = UserSerializer

user_list = UserListAPIView.as_view()


class UserDetailAPIView(RetrieveAPIView):

    permission_classes = (IsAdminOrOwner,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'
    # lookup_url_kwarg = 'name'

user_detail = UserDetailAPIView.as_view()


class UserCreateAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer
    # lookup_field = 'username'
    # lookup_url_kwarg = 'name'

user_create = UserCreateAPIView.as_view()


class UserUpdateAPIView(UpdateAPIView):

    permission_classes = (IsAdminOrOwner,)
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer
    # lookup_field = 'username'
    # lookup_url_kwarg = 'name'

user_update = UserUpdateAPIView.as_view()


class UserDeleteAPIView(DestroyAPIView):

    permission_classes = (IsSuperuser,)
    queryset = User.objects.all()
    # serializer_class = UserSerializer
    # lookup_field = 'username'
    # lookup_url_kwarg = 'name'

user_delete = UserDeleteAPIView.as_view()


