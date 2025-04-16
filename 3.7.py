import math
def teilor(x):
    x = x - (2 * math.pi) * int(x / (2 * math.pi))
    sinx = 0
    i = 0
    element = x
    while sinx + element != sinx:
        sinx += element
        i += 2
        element = element * x * x / (i * (i+1)) * (-1)
    return sinx

print('print angle(rad)')
x = float(input())
s1 = teilor(x)
s2 = math.sin(x)
print('x1=', s1)
print('x2=', s2)
print('error', abs(s1 -s2))