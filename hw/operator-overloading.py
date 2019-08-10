class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Point(x, y)

    def __mul__(self, other):
        x = self.x * other.x
        y = self.y * other.y
        return Point(x, y
                     )


p1 = Point(5, 6)
p2 = Point(2, 3)
p3 = p1 + p2
print(p3.x, p3.y)

p4 = p1 - p2
print(p4.x, p4.y)

p5 = p1 * p2
print(p5.x, p5.y)
