import math
class Point:
    '''для работы с точкой'''
    def __init__ (self , x1 , y1):
        self.x1 = x1
        self.y1 = y1
        print("point" , x1 , y1)
        print(x1 * y1)
    def f(self):
        print(self.x1 + self.y1)
class Rect(Point):
    '''прямоугольный класс'''
    def __init__ (self , x1 , y1 , x2 , y2):
        super().__init__(x1,y1)
        self.x2 = x2
        self.y2 = y2
        print("Rect")
        print(abs(x1 - x2) * abs(y1 - y2))
class Coordx(Point):
    '''находит координату х у точки'''
    def __init__ (self, x1):
        super(). __init__ (x1 , x1)
        self.x1 = x1
        print("class coord" , x1)
class Triangle(Point):
    '''определяет координаты трех точек треугольника'''
    def __init__ (self, x1 , y1 , x2 , y2 , x3 , y3 , q , w , e):
        super(). __init__ (x1 , y1)
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.q = q
        self.w = w
        self.e = e
        q = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        w = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
        e = math.sqrt((x3 - x1) ** 2 + (y3 - y1) ** 2)
        if q + w > e and q + e > w and w + e > q:
            print("class triangle True")
        else:
            print("class triangle False")

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x3 = int(input())
y3 = int(input())
q = 0
w = 0
e = 0
a = Point(x1 , y1)
b = Rect(x1 , y1 , x2 , y2)
c = Coordx(x1)
d = Triangle(x1 , y1 , x2 , y2 , x3 , y3 , q , w , e)



