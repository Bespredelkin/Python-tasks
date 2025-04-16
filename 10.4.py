import numpy as np
class Matrix:
    '''matrix'''
    def __init__ (self , a , b ):
        self.a = a
        self.b = b
    def deystvia(self , a , b):
        a = np.array([[1, 2, 3], [4, 5, 6]], float)
        b = np.array([[3, 4, 5], [1, 2, 3]], float)
        print(np.add(a, b))
        print(np.subtract(a, b))
        print(np.multiply(a, b))
        print(np.divide(a, b))
        print(np.transpose(a))
        print(np.transpose(b))
a = 0
b = 0
opred = Matrix(a , b)
opred.deystvia(opred.a , opred.b)
