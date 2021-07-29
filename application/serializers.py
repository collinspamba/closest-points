"""Module to define our model serializer
"""
from rest_framework import serializers
from .models import ClosestPoints
from . import calculate

class ClosestPointsSerializer(serializers.ModelSerializer):
    """Serializer class for ClosestPoints model
    """
    class Meta:
        """Serializer meta class
        """
        model = ClosestPoints
        fields = ['points_string', 'closest_pair']
        read_only_fields = ['closest_pair'] # to be calculated

    def create(self, validated_data):
        """Handle model object creation
        """
        # the validated points string
        points_string = validated_data.get('points_string')

        # calculate the closest pair
        closest_pair =  calculate.closest_pair(points_string)

        # save the data
        return ClosestPoints.objects.create(
            points_string=points_string,
            closest_pair=closest_pair
        )

    def validate_points_string(self, value):
        """Validate the points string submitted
        is what we expect
        """
        # ensure its a string of points
        if not isinstance(value, str) or len(value) < 11:
            raise serializers.ValidationError('Enter a valid points string')

        # is valid
        return value
