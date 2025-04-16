import numpy as np
class Massive:
    '''Massive'''
    def __init__ (self , a):
        self.a = a
    def deystvia(self , a):
        a = []
        for i in list:
            a = np.append(a,int(i))
        if len(a) % 3 == 1:
            print("write 2 numbers")
            a = np.append(input())
            a = np.append(input())
        elif len(a) % 3 == 2:
            print("write 1 number")
            a = np.append(input())
        a = np.reshape(3,len(a)//3)
        for i in a:
            a1 = i
            a2 = i+1
            a3 = i+2
        b = np.column_stack(a1 , a2 , a3)
        print(b)
        #print(b.min(), b.max())


list = input().split()
a = 0
opred = Massive(a)
opred.deystvia(opred.a)
a1=0
a2=0
a3=0