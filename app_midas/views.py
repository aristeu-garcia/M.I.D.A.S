# from rest_framework import generics
# from .models import Users
# from .serializers import Serializer
from django.shortcuts import render, HttpResponse

# class UserModelListView(generics.ListAPIView):
#     queryset = Users.objects.all()
#     serializer_class = Serializer


def index(request):
    return render(request, "app_midas/index.html")