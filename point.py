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