from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Site, Token, Commodity, Strategy, Group


Client = get_user_model()

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'name', 'email', 'cellphone', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = Client.objects.create_user(
            name=validated_data['name'],
            email=validated_data['email'],
            username=validated_data['email'], 
            cellphone=validated_data['cellphone'], 
            password=validated_data['password'],
        )
        return user


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('id', 'site', 'client')
        
    def create(self, validated_data):
        # Acessa o usuário atualmente autenticado
        user = self.context['request'].user
        # Atribui o ID do usuário ao campo desejado
        validated_data['client'] = user
        # Cria o objeto com os dados validados
        return super().create(validated_data)
        
        
class TokenSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Token
        fields = ('id', 'token', 'client')
        
    def create(self, validated_data):
        # Acessa o usuário atualmente autenticado
        user = self.context['request'].user
        # Atribui o ID do usuário ao campo desejado
        validated_data['client'] = user
        # Cria o objeto com os dados validados
        return super().create(validated_data)
        
        
class CommoditySerializer(serializers.ModelSerializer):
    class Meta:
        model = Commodity
        fields = ('id', 'name', 'code', 'client')
        
    def create(self, validated_data):
        # Acessa o usuário atualmente autenticado
        user = self.context['request'].user
        # Atribui o ID do usuário ao campo desejado
        validated_data['client'] = user
        # Cria o objeto com os dados validados
        return super().create(validated_data)
        
        
class StrategySerializer(serializers.ModelSerializer):
    class Meta:
        model = Strategy
        fields = ('id', 'name', 'client', 'commodity', 'tokens', 'sites')
        
    def __init__(self, *args, **kwargs):
        super(StrategySerializer, self).__init__(*args, **kwargs)
        user = self.context['request'].user 
        self.fields['commodity'].queryset = Commodity.objects.filter(client=user)
        
    def create(self, validated_data):
        user = self.context['request'].user        
        validated_data['client'] = user
        return super().create(validated_data)
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = instance.client.name
        representation['commodity'] = instance.commodity.name 
        representation['tokens'] = [token.token for token in instance.tokens.all()]
        representation['sites'] = [site.site for site in instance.sites.all()]
        return representation
        
        
class GroupSerializer(serializers.ModelSerializer):
    admin = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    participants = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), many=True)
    
    class Meta:
        model = Group
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['admin'] = instance.client.name 
        representation['participants'] = instance.client.name 
        return representation