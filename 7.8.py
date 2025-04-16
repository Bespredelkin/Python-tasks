import numpy as np
a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
c = [([0] * len(a)) for i in range(len(b[0]))]

for i in range(len(a)):
    for j in range(len(b[0])):
        for k in range(len(a[0])):
            c[i][j] += a[i][k] * b[k][j]
print(c)
print(np.dot(a,b))