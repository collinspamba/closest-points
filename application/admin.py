"""Application admin models"""
from django.contrib import admin
from .models import ClosestPoints
from . import calculate


# register ClosestPoints model
@admin.register(ClosestPoints)
class ClosestPointsAdmin(admin.ModelAdmin):
    """ClosestPoints Model Admin"""
    # list display
    list_display = ('points_string', 'closest_pair', 'added')

    # fields in forms
    fields = ('points_string', 'closest_pair')

    # closest_pair is a read only field
    readonly_fields = ('closest_pair',)

    # fields ordering
    ordering = ('added',)

    # show calculated closest pair
    @admin.display(description='Closest Pair')
    def closest_pair(self, instance):
        """Calculate closest pair"""
        return calculate.closest_pair(instance.points_string)
