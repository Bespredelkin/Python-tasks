
def sum(a,b,c,d):
    global real
    global image
    real = a + c
    image = b + d
    return real, image
def mins(a,b,c,d):
    global real
    global image
    real = a - c
    image = b - d
    return real, image
def prois(a,b,c,d):
    global real
    global image
    real = a * c + b * d
    image = a * d + c * b
    return real, image
def delen(a,b,c,d):
    global real
    global image
    real = a // c + b // d
    image = a // d + b // c
    return real, image
def a(x,y):
    return x+y
def b(x,y):
    return x*y
def c(x,y):
    return x/y
def d(x,y):
    return x-y
x=complex(input())
y=complex(input())
print(a(x,y))
print(b(x,y))
print(c(x,y))
print(d(x,y))

real = 0
image = 0
a=float(input())
b=float(input())
c=float(input())
d=float(input())
sum(a,b,c,d)
print('Sum = ', sum(a,b,c,d))
print('mins = ', mins(a,b,c,d))
print('prois = ', prois(a,b,c,d))
print('delen = ', delen(a,b,c,d))