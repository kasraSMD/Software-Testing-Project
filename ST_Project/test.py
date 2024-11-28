import unittest
class TestCalculateAreaAndPerimeter(unittest.TestCase):
    def test_rectangle_with_positive_values(self):
        length = 5
        width = 3
        expected_area = 15
        expected_perimeter = 16
        area, perimeter = calculate_area_and_perimeter(length, width)
        self.assertEqual(area, expected_area)
        self.assertEqual(perimeter, expected_perimeter)