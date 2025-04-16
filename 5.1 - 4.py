import math
a = input()
b = input()
c = input()
try:
    a = int(a)
    b = int(b)
    c = int(c)
    math.sqrt(a - b) + math.log(a, math.e) - (a + b) / c
except (ZeroDivisionError , ValueError , TypeError):
    print('Введены некорректные данные')
else:
    a = int(a)
    b = int(b)
    c = int(c)
    x = (a - b) ** 0.5 + math.log(a, math.e) - (a + b) / c
    print (x)

