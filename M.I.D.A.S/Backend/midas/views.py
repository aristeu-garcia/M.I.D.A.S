from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class RegisterView(APIView):
    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class SiteViewSet(viewsets.ModelViewSet):
    serializer_class = SiteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Acessa o usuário logado através do objeto request
        logged_client = self.request.user
        # Filtra os commodities para retornar apenas aqueles que têm a chave estrangeira igual ao ID do usuário logado
        return Site.objects.filter(client=logged_client)
    
    
class TokenViewSet(viewsets.ModelViewSet):
    serializer_class = TokenSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Acessa o usuário logado através do objeto request
        logged_client = self.request.user
        # Filtra os commodities para retornar apenas aqueles que têm a chave estrangeira igual ao ID do usuário logado
        return Token.objects.filter(client=logged_client)
    
    
class CommodityViewSet(viewsets.ModelViewSet):
    serializer_class = CommoditySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Acessa o usuário logado através do objeto request
        logged_client = self.request.user
        # Filtra os commodities para retornar apenas aqueles que têm a chave estrangeira igual ao ID do usuário logado
        return Commodity.objects.filter(client=logged_client)
    
    
class StrategyViewSet(viewsets.ModelViewSet):
    serializer_class = StrategySerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        # Acessa o usuário logado através do objeto request
        logged_client = self.request.user
        # Filtra os commodities para retornar apenas aqueles que têm a chave estrangeira igual ao ID do usuário logado
        return Strategy.objects.filter(client=logged_client)
    
    
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer