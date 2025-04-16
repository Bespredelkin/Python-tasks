class Types:
    '''при инициализации принимает на вход три аргумента - длины сторон треугольника. Если треугольник с такими сторонами не существует, то должно быть выведено сообщение "Треугольник с такими сторонами не существует!!!"'''
    def __init__ (self , a , b , c):
        self.a = a
        self.b = b
        self.c = c
    def check_types(self , a , b , c):
        if a + b > c and a + c > b and b + c > a:
            print('Треугольник с такими сторонами существует!!!')
        else: print('Треугольник с такими сторонами не существует!!!')
a = int(input())
b = int(input())
c = int(input())
opred = Types(a , b , c)
opred.check_types(opred.a , opred.b , opred.c)