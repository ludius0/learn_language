# libs
from numbers import Real
import math

class Vec2():
    """
    The two dimensional vector.
    'vec' is for vector
    'n' is for number
    """
    def __init__(self, x=0., y=0.):
        assert isinstance(x, Real) and isinstance(y, Real)
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vec2({self.x}, {self.y})"
    
    def __len__(self):
        return 2
    
    def __getitem__(self, index):
        assert index in (0, 1, "x", "y")
        return self.x if index in (0, "x") else self.y

    def __add__(self, vec):
        assert isinstance(vec, Vec2)
        return Vec2(self.x + vec[0], self.y + vec[1])

    def __radd__(self, vec):
        return self.__add__(vec)

    def __sub__(self, vec):
        assert isinstance(vec, Vec2)
        return Vec2(self.x - vec[0], self.y - vec[1])

    def __rsub__(self, vec):
        return self.__add__(vec)
    
    def __mul__(self, n):
        assert isinstance(n, Real)
        return Vec2(self.x * n, self.y * n)
    
    def __rmul__(self, n):
        return self.__mul__(n)
    
    def __truediv__(self, n):
        assert isinstance(n, Real)
        return Vec2(self.x / n, self.y / n)

    def __rtruediv__(self, n):
        return self.__div__(n)

    def __floordiv__(self, n):
        assert isinstance(n, Real)
        return Vec2(self.x // n, self.y // n)

    def __rfloordiv__(self, n):
        return self.__floordiv__(n)
    
    def __eq__(self, vec):
        assert isinstance(vec, Vec2)
        return self.x == vec[0] and self.y == vec[1]
    
    def __matmul__(self, vec):
        assert isinstance(vec, Vec2)
        return Vec2(self.x * vec[0], self.y * vec[1])
    
    def dot(self, vec):
        return self.__matmul__(vec)
    
    
    @property
    def lenght(self):
        return math.sqrt(self.x ** 2 + self.y ** 2) # math.hypot()
    
    @property
    def length_sqrd(self):
        return self.x ** 2 + self.y ** 2
    
    @staticmethod
    def zeros():
        return Vec2(0., 0.)