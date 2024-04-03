from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from midas.views import *


router = DefaultRouter()
router.register('sites', SiteViewSet, basename='sites')
router.register('tokens', TokenViewSet, basename='tokens')
router.register('commodity', CommodityViewSet, basename='commodity')
router.register('strategy', StrategyViewSet, basename='strategy')
router.register('group', GroupViewSet, basename='group')


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]