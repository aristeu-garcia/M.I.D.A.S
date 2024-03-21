from rest_framework import viewsets, generics
from midas.serializers import ClientSerializer
from midas.models import Client

class ClientsViewSet(viewsets.ModelViewSet):
    """Exibindo todos os clientes"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer