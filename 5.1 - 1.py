class Types:
    '''Если аргументы одного типа, то выводится сумма этих аргументов. Если же аргументы различного типа, то выводится текстовое сообщение 'Введены аргументы различного типа!!!' '''
    def __init__ (self , a , b):
        self.a = a
        self.b = b
    def check_types(self , a , b):
        g = 0
        try:
            a = int(a)
        except ValueError:
            c = 1
        else:
            c = 0
        try:
            b = int(b)
        except ValueError:
            d = 1
        else:
            d = 0
        if d == c:
            print(a + b)
        else:
            print('Введены аргументы различного типа!!!')
a = input()
b = input()
opred = Types(a , b)
opred.check_types(opred.a , opred.b)
