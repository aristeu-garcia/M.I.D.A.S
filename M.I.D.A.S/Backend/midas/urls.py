from django.contrib import admin
from django.urls import path, include
from app_midas.views import ClientView

urlpatterns = [
    path('clients/', ClientView.as_view(), name='clients')
]