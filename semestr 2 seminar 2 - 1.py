from datetime import datetime
n = int(input())
t1 = datetime.now()
def stupenka(n):
    a = [0 for i in range(n+1)]
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        a[0] = 0
        a[1] = 1
        a[2] = 2
        a[3] = 4
        for i in range(4,n+1):
            a[i] = a[i-1] + a[i-2]+ a[i-3]
        return a[n]
print(stupenka(n))
print(datetime.now() - t1)
t2 = datetime.now()
def stupenkaplohaya(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    else:
        return stupenkaplohaya(n-1) + stupenkaplohaya(n-2) + stupenkaplohaya(n-3)
print(stupenkaplohaya(n))
print(datetime.now() - t2)