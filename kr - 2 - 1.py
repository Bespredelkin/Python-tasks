a = list(map(int, input().split()))
max = 0
elements = []
for i in range(0, len(a)):
    for j in range(i +1, len(a)):
        if max <= abs(a[i] * a[j]):
            max = abs(a[i] * a[j])
            elements = []
            elements.append(a[i])
            elements.append(a[j])

print(elements[0], elements[1])

