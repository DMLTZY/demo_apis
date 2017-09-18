from rest_framework.authtoken.models import Token
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
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        gender = validated_data.get('gender')
        user = User(username=username,
                    email=email,
                    password=password,
                    gender=gender)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return validated_data


class UserDetailSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'gender')

