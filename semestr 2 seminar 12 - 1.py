file1 = open('12-1.txt')
file2 = open('12-1.txt')

a = file1.readline()
n, m = map(int, a.split())
b = file2.readline()
n, m = map(int, a.split())
G = [[0]*n for _ in range(n)]
GG = {}
V = []
for _ in range(m):
    a = file1.readline()
    v1, v2 = a.split()
    for v in (v1, v2):
        if v not in V:
            V.append(v)
    G[V.index(v1)][V.index(v2)] = 1

for _ in range(m):
    b = file2.readline()
    v1, v2 = b.split()
    GG.setdefault(v1, set()).add(v2)


print()
for i in range(n):
    for j in range(m):
        print(G[i][j], end=' ')
    print()
print()
print(GG)