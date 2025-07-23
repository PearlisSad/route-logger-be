from rest_framework import viewsets
from .models import Wall, Route
from .serializers import WallSerializer, RoutesSerializer

class WallViewSet(viewsets.ModelViewSet):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer

class RoutesViewSet(viewsets.ModelViewSet):
    queryset = Route.objects.all()
    serializer_class = RoutesSerializer
