a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
d = []
e = []
f = 0
for i in range(a, b, c):
    d.append(i)
for j in d:
    if d[j-1] % 2 != 0:
        e.append(d[j-1])
for k in range(0 , len(e)):
    f = f + e[k]
g = int((f / len(e)) // 1)
print(g)
print(e[len(e)-1])
if len(e) == 1: print(0)
elif len(e) == 0 : print(-1)