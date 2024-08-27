class Point(tuple):
    def __new__(cls, x, y, id = -1):
        return super().__new__(cls, (x, y))

    def __init__(self, x, y, id = -1):
        self.x = x
        self.y = y
        self.id = id
    
    def __repr__(self):
        return f"{self.id}:({self.x},{self.y})"
    
class Intersection(Point):
    def __new__(cls, x, y , road1, road2):
        return super().__new__(cls, x, y)
    
    def __init__(self, x, y, road1, road2):
        super().__init__(x, y)
        self.road1 = road1
        self.road2 = road2

    def __repr__(self):
        return f"{super().__repr__()} road1: {self.road1} road2:{self.road2}"
        
if __name__ == "__main__":
    a = Point(1, 2)
    b = Point(3, 4, 5)
    c = Intersection(5, 6, "A", "B")

    print(a)
    print(repr(a))
    print(b)
    print(c)