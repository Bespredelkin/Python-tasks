class Rects:
    '''Родитель четырехугольников'''
    def __init__ (self , a , b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    def mazaika(self):
        return self.a + self.b + self.c + self.d
class square(Rects):
    '''квадрат'''
    def __init__ (self , a ):
        super().__init__(a, a, a, a)
    def ploshch(self):
        return self.a*self.a
class tra(Rects):
    '''трапеция'''
    def __init__ (self , a , b , c ,d ,h):
        super().__init__(a , b, c, d)
        self.h = h
    def ploshch(self):
        return (self.a+self.b)/2 * self.h
class Pra(Rects):
    '''прямоугольник'''
    def __init__ (self , a , b):
        super().__init__(a , b, a, b)
    def ploshch(self):
        return self.a * self.b

a = int(input())
b = int(input())
h = int(input())
sq = square(a)
tr = tra(a, b, h, h, h)
pr = Pra(a, b)
print("Квадрат: ", sq.ploshch(), "  ", sq.mazaika())
print("Прямоугольник: ", pr.ploshch(), "  ", pr.mazaika())
print("Трапеция: ", tr.ploshch() )
