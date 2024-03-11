from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Client
from .serializers import ClientSerializer
from rest_framework import viewsets

class ClientView(viewsets.ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        # Aqui você pode aplicar qualquer lógica que desejar para determinar o queryset
        # Por exemplo, filtrar os clientes com base em algum critério
        return Client.objects.filter()
    def get(self, request):
        users = Client.objects.all()
        serializer = ClientSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        user = Client.objects.get(id=id)
        serializer = ClientSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        user = Client.objects.get(id=id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)