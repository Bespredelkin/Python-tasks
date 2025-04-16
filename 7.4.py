a = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
n = len(a)
m = len(a[0])
imax = 0
imin = 0
emax = a[0][0]
emin = a[0][0]
for i in range(n):
    for j in range(m):
        if a[i][j] > emax:
            emax = a[i][j]
            imax = i
        if a[i][j] < emin:
            emin = a[i][j]
            imin = i
for j in range(n):
    t = a[imin][j]
    a[imin][j] = a[imax][j]
    a[imax][j] = t
print(a)


