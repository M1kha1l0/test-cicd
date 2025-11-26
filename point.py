import math
import unittest

class Point:
    __x = float()
    _Point__y = float()

    def __init__(self, x: float, y: float):
        self.__x = x
        self._Point__y = y
    
    def __str__(self):
        return f"({self.__x}; {self._Point__y})"
    
    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.__x == other.__x and self._Point__y == other._Point__y

    @staticmethod
    def dist(A, B):
        return math.sqrt((A.__x - B.__x)**2 + (A.__y - B.__y)**2)
    
    @staticmethod
    def center(A, B):
        C = Point((A.__x + B.__x) / 2, (A.__y + B.__y) / 2)
        return C
    
class PointTestCase(unittest.TestCase):
    def test_distance(self):
        a = Point(1, 1)
        b = Point(4, 3)
        self.assertAlmostEqual(Point.dist(a, b), 3.6055, delta=0.0001)

    def test_points_on_line_x_distance(self):
        a = Point(1, 1)
        b = Point(1, 4)
        self.assertEqual(Point.dist(a, b), 3)

    def test_points_on_line_y_distance(self):
        a = Point(1, 4)
        b = Point(6, 4)
        self.assertEqual(Point.dist(a, b), 5)

    def test_null_distance(self):
        a = Point(1, 1)
        self.assertEqual(Point.dist(a, a), 0)
    
    def test_equal_int(self):
        a = Point(1, 1)
        self.assertEqual(a, Point(1, 1))

    def test_equal_float(self):
        a = Point(1.12, 1.2)
        self.assertEqual(a, Point(1.12, 1.2))

    def test_center(self):
        a = Point(1, 1)
        b = Point(4, 3)
        self.assertEqual(Point.center(a, b), Point(2.5, 2))
    
    def test_center_in_point(self):
        a = Point(1, 2)
        self.assertEqual(Point.center(a, a), a)

    def test_points_on_line_x(self):
        a = Point(1, 4)
        b = Point(1, 8)
        self.assertEqual(Point.center(a, b), Point(1, 6))
    
    def test_points_on_line_y(self):
        a = Point(4, 4)
        b = Point(10, 4)
        self.assertEqual(Point.center(a, b), Point(7, 4))
    
    def test_str_not_empty(self):
        a = Point(1, 1)
        self.assertTrue(a.__str__)