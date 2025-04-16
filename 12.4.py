a = [2, 4, 5, 8, 9, 9, 9, 11, 11, 11, 11, 13, 13, 115, 115]
x = int(input())
def nachalo(a,x):
    n = len(a)
    k = n
    l = -1
    m = (n) // 2
    while k - l > 1:
        m = (k+l) // 2
        if a[m - 1] < x:
            l = m
        else:
            k = m
    return l
def konets(a,x):
    n = len(a)
    k = n
    l = -1
    m = (n) // 2
    while k - l > 1:
        m = (k+l) // 2
        if a[m] <= x:
             l = m
        else:
             k = m
    return l
print(nachalo(a, x))
print(konets(a, x))