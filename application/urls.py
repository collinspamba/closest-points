"""application URLs
"""
from django.urls import path, include
from rest_framework import routers
from .views import HomePage, ClosestPointsViewSet

# define the api router
router = routers.DefaultRouter()
router.register(r'closestpoints', ClosestPointsViewSet)

# define the urlpatterns
app_name = 'application'
urlpatterns = [
    path('', HomePage.as_view(), name='homepage'), # home page
    path('api/', include((router.urls, 'application'), namespace='api')), # api
]
