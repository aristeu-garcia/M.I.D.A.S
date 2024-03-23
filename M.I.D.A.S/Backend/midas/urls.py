from django.urls import path
from rest_framework.routers import DefaultRouter
from app_midas.views import ClientView

router = DefaultRouter()
router.register(r'clients', ClientView, basename='clients')

urlpatterns = router.urls
