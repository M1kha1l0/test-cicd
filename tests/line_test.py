import unittest
import math

from src.line import Line
from src.point import Point

class LineTestCase(unittest.TestCase):
    def test_equal(self):
        f = Line.from_points(Point(0, 0), Point(1, 2))
        g = Line(2, 0)
        h = Line(2, 1)
        self.assertEqual(f, g)
        self.assertNotEqual(f, h)
        self.assertNotEqual(g, h)
    
    def test_not_null_str(self):
        f = Line.from_points(Point(0, 0), Point(1, 2))
        g = Line(2, 0)
        self.assertTrue(str(f) != "") 
        self.assertTrue(str(g) != "")

    def test_on_line(self):
        f = Line.from_points(Point(0, 0), Point(1, 2))
        self.assertTrue(f.contains(Point(2, 4)))
        self.assertTrue(f.contains(Point(-2, -4)))
        self.assertFalse(f.contains(Point(1, 0)))

    def test_calc_y(self):
        f = Line(2, 0)
        self.assertEqual(f.Y(2), 4)
        self.assertEqual(f.Y(-2), -4)
        self.assertNotEqual(f.Y(-2), -5)

    def test_calc_x(self):
        f = Line(2, 0)
        self.assertEqual(f.X(4), 2)
        self.assertEqual(f.X(-4), -2)
        self.assertNotEqual(f.X(-4), -1)

    def test_vertical_line(self):
        vertical = Line.from_points(Point(3, 0), Point(3, 5))
        self.assertTrue(math.isinf(vertical._Line__k))
        self.assertTrue(vertical.contains(Point(3, 10)))
        self.assertFalse(vertical.contains(Point(4, 10)))
        
        self.assertAlmostEqual(vertical.X(100), 3, places=10)