n = int(input())
a = 0
b = 1
c = 1
d = [a, b , c]
while c < n-2:
    a = b
    b = c
    c = a+b
    d.append(c)
print(d)