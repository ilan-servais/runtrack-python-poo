class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Afficher(self):
        return f"({self.x}, {self.y})"


point1 = Point(10, 20)
point2 = Point(30, 40)

print(point1.Afficher())
print(point2.Afficher())
