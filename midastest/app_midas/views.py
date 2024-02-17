from rest_framework import generics
from .models import Users
from .serializers import Serializer

class UserModelListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = Serializer
