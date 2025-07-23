from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Route, Wall
from .serializers import RouteSerializer, WallSerializer

class RoutesViewSet(viewsets.ModelViewSet):
    serializer_class = RouteSerializer
    queryset = Route.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset()
        wall_id = self.request.query_params.get('wall')
        if wall_id is not None:
            queryset = queryset.filter(wall=wall_id)
        return queryset


class WallViewSet(viewsets.ModelViewSet):
    queryset = Wall.objects.all()
    serializer_class = WallSerializer

