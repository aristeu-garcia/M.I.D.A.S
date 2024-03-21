from django.contrib import admin
from django.urls import path, include
from midas.views import ClientsViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('clients', ClientsViewSet, basename='Clients')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]