"""application tests
"""
from django.test import TestCase
from .calculate import closest_pair, generate_tuples_list_from_string, square


class ClosestPointsTestCase(TestCase):
    """Test functions calculating the closest points pair
    """
    def test_closest_pair(self):
        """Test closest pair function
        """
        points_string = '(45,12),(54.32,189.43),(94,19),(871,320)'
        closest_points_pair = closest_pair(points_string)
        self.assertEqual(closest_points_pair, '(45, 12),(94, 19)')

    def test_generate_list_from_string(self):
        """Test generate list from string function
        """
        points_string = '(45,12),(54.32,189.43),(94,19),(871,320)'
        points_list = generate_tuples_list_from_string(points_string)
        self.assertEqual(points_list, [(45, 12), (54.32, 189.43), (94, 19), (871, 320)])

    def test_squares(self):
        """Test squares function
        """
        self.assertEqual(square(2), 4)
