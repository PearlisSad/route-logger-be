from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WallViewSet, RoutesViewSet

router = DefaultRouter()
router.register(r'walls', WallViewSet)
router.register(r'route', RoutesViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
