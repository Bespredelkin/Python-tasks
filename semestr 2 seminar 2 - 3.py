def stupenka(n):
    a = [0 for i in range(n+1)]
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 4
    if n == 3:
        return 7
    else:
        a[0] = 0
        a[1] = 2
        a[2] = 4
        a[3] = 7
        for i in range(4,n+1):
            a[i] = a[i-1] + a[i-2]+ a[i-3]
        return a[n]
n = int(input())
print(stupenka(n))