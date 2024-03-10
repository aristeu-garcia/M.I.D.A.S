from django.contrib import admin
from django.urls import path, include
from app_midas.views import UserModelListView

urlpatterns = [
    path('users/', UserModelListView.as_view(), name='users'),
    path("admin/", admin.site.urls)
]