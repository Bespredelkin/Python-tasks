n = 5
mat = [[2] * n for i in range(n)]
a = []
for i in range(n):
    c = 0
    for j in range(n):
        c += mat[i][j]
    a.append(c)
b = 0
for i in range(n):
    b += mat[i][i]
a.append(b)
d = 0
for i in range(n):
    d += mat[n-i-1][i]
a.append(d)
print(a)