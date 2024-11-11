from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import User


class LogSerializer(serializers.Serializer):
    # Для авторизациии
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
        attrs['user'] = user
        return attrs


class RegSerializer(serializers.ModelSerializer):
    # для регистрации
    password = serializers.CharField(min_length=12)

    class Meta:
        model = User
        fields = ['email', 'password', 'fio']

    def save(self, **kwargs):
        user = User()
        user.email = self.validated_data['email']
        user.fio = self.validated_data['fio']
        user.set_password(self.validated_data['password'])
        user.save()
        return user
