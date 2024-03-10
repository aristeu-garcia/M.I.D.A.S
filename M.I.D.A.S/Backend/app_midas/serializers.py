from rest_framework import serializers
from .models import Client,ClientGroup


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'name', 'email']


class ClientGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientGroup
        fields = '__all__'