import math
print('print angle(rad)')
x = float(input())
x = x-(2 * math.pi)*int(x / (2 * math.pi))
sinx = 0
i = 0
element = x
while sinx+element != sinx:
    sinx += element
    i += 2
    element = element*x*x/(i*(i+1)) * (-1)
print(sinx, math.sin(x))
