a = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
n = len(a)
m = len(a[0])
for i in range(n):
    for j in range(i):
        t = a[i][j]
        a[i][j] = a[j][i]
        a[j][i] = t
print(a)