a = [5,4,56,3,6,3,1,2]
for i in range(len(a)-1):
    for j in range(len(a)-1 - i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
a[0], a[len(a) - 1] = a[len(a) - 1], a[0]
print(a)
