import math
from point import Point

class Line:
    def __init__(self, k: float, b: float):
        self.__k = k
        self.__b = b

    @classmethod
    def from_points(cls, point1: Point, point2: Point):
        x1 = point1._Point__x
        y1 = point1._Point__y
        x2 = point2._Point__x
        y2 = point2._Point__y
        
        if x1 == x2:
            k = math.inf
            b = x1
        else:
            k = (y1 - y2) / (x1 - x2)
            b = y1 - k * x1
        
        return cls(k, b)
    
    def __str__(self) -> str:
        if math.isinf(self.__k):
            return f"x = {self.__b}"
        elif self.__b >= 0:
            return f"f(x) = {self.__k}*x + {self.__b}"
        else:
            return f"f(x) = {self.__k}*x - {abs(self.__b)}"
    
    def __eq__(self, other):
        if not isinstance(other, Line):
            return False
        
        tolerance = 1e-10
        if math.isinf(self.__k) and math.isinf(other.__k):
            return abs(self.__b - other.__b) < tolerance
        elif math.isinf(self.__k) or math.isinf(other.__k):
            return False
        else:
            return (abs(self.__k - other.__k) < tolerance and 
                    abs(self.__b - other.__b) < tolerance)

    def Y(self, x: float) -> float:
        if math.isinf(self.__k):
            raise ValueError("Vertical line: cannot calculate Y for given X")
        return self.__k * x + self.__b
    
    def X(self, y: float) -> float:
        if math.isinf(self.__k):
            return self.__b
        return (y - self.__b) / self.__k
    
    def contains(self, point: Point) -> bool:
        px = point._Point__x
        py = point._Point__y
        
        if math.isinf(self.__k):
            return abs(px - self.__b) < 1e-10
        else:
            return abs(py - self.Y(px)) < 1e-10