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
            imax = j
        for k in range(n):
            emin = emax
            if a[k][imax] > emin:
                emin = a[k][imax]
                imin = i
        if emax == emin:
            print(emax)
            break
