from djoser.serializers import (
    UserCreateSerializer as BaseUserCreateSerializer,
    UserSerializer as BaseUserSerializer,
    
)

from rest_framework import serializers


class UserCreateSerializer(BaseUserCreateSerializer):
    """ Overriding user create serializer """

    class Meta(BaseUserCreateSerializer.Meta):

        fields = ['id', 'username', 'password', 
                   'email', 'first_name', 'last_name']

class UserSerializer(BaseUserSerializer):
    """ Overriding current user serializer """

    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'email', 'username', 'first_name', 'last_name']