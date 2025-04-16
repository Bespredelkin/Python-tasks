'''
print("введите клетку на которой стоит ферзь")
a = int(input())
b = int(input())
print("введите клетку куда ферзь мог пойти")
c = int(input())
d = int(input())
if a == c or b == d:
    print('да')
elif abs(a - c) == abs(b - d):
    print('да')
else: print('хаха , он не умеет играть в шахматы')
'''

m = 8
n = 8
mat = [[0] * m for i in range (n)]
print(mat)
print("введите клетку на которой стоит ферзь")
x1 = int(input())
y1 = int(input())
for i in range(n):
    for j in range(m):
        if i == x1 or j == y1 or i - x1 == j - y1:
            mat[i][j] = 1
print(mat)
print("введите клетку куда ферзь мог пойти")
x2 = int(input())
y2 = int(input())
if mat[x2][y2] == 1:
    print('да')
else: print('хаха , он не умеет играть в шахматы')
