from rest_framework import serializers
from .models import *

class SiteSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    
    class Meta:
        model = Site
        fields = '__all__'
        
        
class TokenSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    
    class Meta:
        model = Token
        fields = '__all__'
        
        
class CommoditySerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    
    class Meta:
        model = Commodity
        fields = '__all__'
        
        
class StrategySerializer(serializers.ModelSerializer):
    commodity = serializers.PrimaryKeyRelatedField(queryset=Commodity.objects.all())
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    tokens = serializers.PrimaryKeyRelatedField(queryset=Token.objects.all(), many=True)
    sites = serializers.PrimaryKeyRelatedField(queryset=Site.objects.all(), many=True)
    
    class Meta:
        model = Strategy
        fields = '__all__'
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['client'] = instance.client.name 
        representation['commodity'] = instance.commodity.name 
        representation['tokens'] = instance.token.token 
        representation['sites'] = instance.site.site 
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