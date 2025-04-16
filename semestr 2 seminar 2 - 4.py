import random
def stupenka(n,b):
    if n == 0:
        return b[0]
    if n == 1:
        return b[0] + b[1]
    if n == 2:
        return b[0] + b[2]
    else:
        a = [0 for i in range(n+1)]
        a[0] = b[0]
        a[1] = b[0] + b[1]
        a[2] = b[0] + b[2]
        for i in range(3, n+1):
           if a[i - 2] > a[i - 1]:
               a[i] = a[i-1] + b[i]
           else:
               a[i] = a[i-2] + b[i]
        return a[n]
n = int(input())
b = [random.randrange(1,n+1,1) for i in range(n+1)]
print(str(stupenka(n,b)) + ' deneg')
print(b)
