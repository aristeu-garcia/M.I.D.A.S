from rest_framework import serializers
from .models import Client,ClientGroup


class ClientSerializer(serializers.ModelSerializer):
    # TODO: Adicionar a seguinte expressão depois: 
    # password = serializers.CharField(write_only=True)
    class Meta:
        
        model = Client
        fields = ['id', 'name', 'email', 'password']


class ClientGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientGroup
        fields = '__all__'