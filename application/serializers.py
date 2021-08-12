"""Module to define our model serializer
"""
from django.core.exceptions import NON_FIELD_ERRORS, ValidationError
from rest_framework import serializers
from .models import ClosestPoints

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

        # create and save model instance
        closest_points = ClosestPoints(points_string=points_string)
        closest_points.save() # closest pair calculated here

        # return
        return closest_points

    def validate_points_string(self, value):
        """Validate the points string submitted
        is what we expect
        """
        # use the validation on the model object
        closest_point = ClosestPoints(points_string=value)

        # passes value through to the Model.clean()
        try:
            closest_point.full_clean()
        except ValidationError as e:
            non_field_errors = e.message_dict[NON_FIELD_ERRORS]
            raise serializers.ValidationError(non_field_errors[0])

        # is valid
        return value
