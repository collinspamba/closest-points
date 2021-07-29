"""application Views
"""
from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .models import ClosestPoints
from .serializers import ClosestPointsSerializer


class HomePage(View):
    """Homepage view
    """
    def get(self, request):
        """Homepage GET request
        """
        return render(request, 'application/home.html')

class ClosestPointsViewSet(viewsets.ModelViewSet):
    """ViewSet to handle views for our closestpoints endpoint
    """
    queryset = ClosestPoints.objects.all()
    serializer_class = ClosestPointsSerializer
