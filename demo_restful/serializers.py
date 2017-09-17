from rest_framework.serializers import ModelSerializer
from user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_superuser',
                  'is_active', 'gender', 'date_joined',)


class UserCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'gender')


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'gender')

