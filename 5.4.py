import math
x = input()
try:
    x = int(x)
    m = math.sqrt((((math.sin(x) ** 2) + (math.cos(x ** 5))) / math.sqrt( math.pi + (math.tan(((x +5)**3) / x)))))
except (ZeroDivisionError , ValueError , TypeError):
    print('Введены некорректные данные')
else:
    print (m)