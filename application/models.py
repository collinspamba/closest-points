"""application Models
"""
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from . import calculate


class ClosestPoints(models.Model):
    """ClosestPoints Table
    Store points requests, calculation results
    """
    points_string = models.TextField()
    closest_pair = models.TextField(blank=True, null=True)
    added = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        """Return the model's string representation"""
        return "\nPoints String: " + self.points_string + "\nClosest Pair: " + str(self.closest_pair)

    def clean(self):
        """Perform model validation"""
        # any points string will be at least 11 characters long
        if not isinstance(self.points_string, str) or len(self.points_string) < 11:
            raise ValidationError(_('Invalid points string'))

        # ensure we can generate a tuples list from this string
        if not calculate.generate_tuples_list_from_string(self.points_string):
            raise ValidationError(_('Invalid points string'))

    def save(self, *args, **kwargs):
        """Override model save operation.
        Perform model validation so that instances are always validated
        regardless of where they were saved i.e API, admin, shells, etc
        """
        # validate the points string
        self.clean()

        # calculate the closest pair
        self.closest_pair = calculate.closest_pair(self.points_string)

        # proceed to save
        super().save(*args, **kwargs)
