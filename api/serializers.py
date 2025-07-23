from rest_framework import serializers
from .models import Wall, Route

class WallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wall
        fields = '__all__'

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = '__all__'
