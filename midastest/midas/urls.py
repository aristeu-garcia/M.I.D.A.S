from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app_midas.views import HealthCheck

# Criar um router
router = DefaultRouter()

# Registrar o HealthCheckView no router
router.register('health-check', HealthCheck, basename='health-check')

# URL patterns
urlpatterns = [
    # Outras URLs podem ser adicionadas aqui
    path('', include(router.urls)),
]
