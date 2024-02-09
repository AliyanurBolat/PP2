class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

A = int(input())
s = Square(A)
print(s.area())

L = int(input())
W = int(input())
area_rec = Rectangle(L, W)
print(area_rec.area())