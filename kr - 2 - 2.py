n = int(input())
a = 0
b = 1
c = 1
d = [c]
s = 0
while len(d) < n:
    a = b
    b = c
    c = a+b
    d.append(c)
for i in range(0, len(d)):
    if d[i] % 2 == 0:
        s += d[i]
print(s)
print(d)