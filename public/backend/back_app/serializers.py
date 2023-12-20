from rest_framework import serializers
from .models import *

class loginSerializer(serializers.ModelSerializer):
    class Meta:
        model=login
        fields='__all__'

class registerSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserRegister
        fields='__all__'


class productSerializer(serializers.ModelSerializer):
    class Meta:
        model=Products
        fields='__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model=productsize
        fields='__all__'

class cartSerializer(serializers.ModelSerializer):
    class Meta:
        model=cart
        fields='__all__'

class favouritetSerializer(serializers.ModelSerializer):
    class Meta:
        model=favourite
        fields='__all__'