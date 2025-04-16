a = list(map(int, input().split()))
min = a[1] + a[2]
elements = []
for i in range(0, len(a)):
    for j in range(i +1, len(a)):
        if min >= a[i] + a[j] and a[i] < a[j]:
            min = a[i] + a[j]
            elements = []
            elements.append(a[i])
            elements.append(a[j])
try:
    print(elements[0], elements[1])
except(IndexError):
    print(-1)
