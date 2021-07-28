"""application Models
"""
from django.db import models


class ClosestPoints(models.Model):
    """ClosestPoints Table
    Store points requests, calculation results
    """
    points_string = models.TextField()
    closest_pair = models.TextField()
