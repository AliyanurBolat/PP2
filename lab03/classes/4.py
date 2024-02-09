import math
class Point():
    def __init__(self):
        self.x_1 = int(input())
        self.y_1 = int(input())
        self.x_2 = int(input())
        self.y_2 = int(input())
        self.pointCoordinates = {self.x_1:self.y_1,}
        self.show()
        self.move()
        self.dist()
    def show(self):
        print(self.pointCoordinates)
    def move(self):
        self.pointCoordinates = {self.x_2:self.y_2,}
    def dist(self):
        self.distance = math.sqrt(pow((self.x_2 - self.x_1), 2) + pow((self.y_2-self.y_1), 2))
        print(self.distance)
n = Point()