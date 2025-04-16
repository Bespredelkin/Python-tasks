def stupenka(n):
    a = [0 for i in range(n+1)]
    if n == 0:
        return 0
    if n == 1:
        return 2
    if n == 2:
        return 3
    else:
        a[0] = 0
        a[1] = 2
        a[2] = 3
        for i in range(3,n+1):
            a[i] = a[i-1] + a[i-2]
        return a[n]
n = int(input())
print(stupenka(n))
