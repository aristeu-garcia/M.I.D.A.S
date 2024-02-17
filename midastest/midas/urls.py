from django.urls import path
from app_midas.views import UserModelListView

urlpatterns = [
    path('users/', UserModelListView.as_view(), name='users'),
]