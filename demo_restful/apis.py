# coding:utf-8
import time
from django.utils import timezone
from django.db.models import Q
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
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
from .paginations import UserPagination
from .permissions import IsSuperuserOrOwner


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


class EchoPost(APIView):
    http_method_names = ['post']
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        data = request.data
        return Response(data=data,
                        status=status.HTTP_200_OK)
        pass

echo_post = EchoPost.as_view()


class UserListAPIView(ListAPIView):

    permission_classes = [IsAdminUser]
    serializer_class = UserSerializer
    pagination_class = UserPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('username', 'email')

    def get_queryset(self):
        queryset = User.objects.all()
        exact_query = self.request.GET.get('q')
        if exact_query:
            queryset = queryset.filter(Q(username=exact_query) |
                                       Q(email__icontains=exact_query))
        return queryset

user_list = UserListAPIView.as_view()


class UserDetailAPIView(RetrieveAPIView):

    permission_classes = (IsSuperuserOrOwner,)
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_field = 'username'

user_detail = UserDetailAPIView.as_view()


class UserCreateAPIView(CreateAPIView):

    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

user_create = UserCreateAPIView.as_view()


class UserUpdateAPIView(UpdateAPIView):

    permission_classes = (IsSuperuserOrOwner,)
    queryset = User.objects.all()
    serializer_class = UserCreateUpdateSerializer

user_update = UserUpdateAPIView.as_view()


class UserDeleteAPIView(DestroyAPIView):

    permission_classes = (IsSuperuserOrOwner,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

user_delete = UserDeleteAPIView.as_view()


