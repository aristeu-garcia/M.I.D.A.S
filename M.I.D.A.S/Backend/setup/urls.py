from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from midas.views import *


router = DefaultRouter()
router.register('sites', SiteViewSet, basename='sites')
router.register('tokens', TokenViewSet, basename='tokens')
router.register('commodities', CommodityViewSet, basename='commodity')
router.register('strategies', StrategyViewSet, basename='strategy')
router.register('groups', GroupViewSet, basename='group')
router.register('clients', ClientViewSet, basename='client')


urlpatterns = [
    path("admin/", admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path("", include(router.urls)),
]