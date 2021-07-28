"""application URLs
"""
from django.urls import path, include
from rest_framework import routers, serializers, viewsets
from .models import ClosestPoints
from .views import homepage


# define the API
class ClosestPointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClosestPoints
        fields = ['points_string', 'closest_pair']
        read_only_fields = ['closest_pair']

# define viewsets
class ClosestPointsViewSet(viewsets.ModelViewSet):
    queryset = ClosestPoints.objects.all()
    serializer_class = ClosestPointsSerializer

# define api router
router = routers.DefaultRouter()
router.register(r'closestpoints', ClosestPointsViewSet)

urlpatterns = [
    path('', homepage, name='homepage'), # home page
    path('api/', include(router.urls)), # api router
]
