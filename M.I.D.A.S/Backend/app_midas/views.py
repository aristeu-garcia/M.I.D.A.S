from rest_framework import generics
from .models import ClientGroup
from .serializers import Serializer
from django.shortcuts import render, HttpResponse

class UserModelListView(generics.ListAPIView):
    queryset = ClientGroup.objects.all()
    serializer_class = Serializer

