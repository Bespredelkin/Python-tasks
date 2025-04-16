#первый способ
a = [[1, 2, 3], [4, 5, 6,], [7, 8, 9]]
print(a)

#второй способ
b = 5
mat = [5] * b
for i in range(b):
    mat[i] = [4] * b
print(mat)

#третий способ
n = 7
m = 4
mat = []
for i in range(n):
    mat.append([14] * m)
print(mat)

#четвертый способ
m = 6
n = 5
mat = [[3] * m for i in range (n)]
print(mat)