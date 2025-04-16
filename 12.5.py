a = [2, 4, 5, 8, 15, 47, 78, 785, 3465]
x = int(input())
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
print(l)