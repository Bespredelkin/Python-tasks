def erot(n):
    a = list(range(n + 1))
    b = []
    a[1] = 0
    for i in a:
        if i > 1:
            for j in range(2*i, len(a), i):
                 a[j] = 0
    for i in range(0, len(a)-1):
        if a[i] != 0:
            b.append(a[i])
    return b
n = int(input())
print(erot(n))