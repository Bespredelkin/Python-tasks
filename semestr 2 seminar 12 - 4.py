f = open('12-1.txt', 'r')
a = f.readline()
n, m = map(int, a.split())
G = [[] for _ in range(n)]
for _ in range (m):
    a = f.readline()
    v1, v2 = map(ord, a.split())
    v1 -= 65
    v2 -= 65
    G[v1].append(v2)
    G[v2].append(v1)
for i, j in enumerate(G):
    print(i, '-', len(j), '=', *j)
