a = [1, 4, 9, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]
a[10] = -50
d = 0
for i in range (0,len(a)-1):
    if a[i] % 2 == 0:
        a[i] = 1
    else:
        a[i] = a[i] / 2
    d += a[i]
for i in range(len(a)-1):
    for j in range(len(a)-1 - i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]


print(a)
print(d)
print('max', a[len(a)-1])
print('min', a[0])