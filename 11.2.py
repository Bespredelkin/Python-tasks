import numpy as np
a = np.array([4, 2, 7])
b = np.array([-4, 3, -3])
c = np.array([-5, 10, -11])
d = np.array([2, 11, 36])
n = int(input())
f = np.array([(int(input())) for i in range(n)])
print(f)
e = [a, b, c]
y = np.linalg.inv(e)
print(np.dot(e, y))
print(np.dot(d, y))
'''matrix = [a,b,c]
matrix1 = [d,b,c]
matrix2 = [a,d,b]
matrix3 = [a,b,d]
delta = np.linalg.det(matrix)
delta1 = np.linalg.det(matrix1)
delta2 = np.linalg.det(matrix2)
delta3 = np.linalg.det(matrix3)
print(delta1/delta)
print(delta2/delta)
print(delta3/delta)'''

