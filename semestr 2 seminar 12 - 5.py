def distance(G):
    n = len(G)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif G[i][j] != 0:
                dist[i][j] = G[i][j]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

f = open('12-1.txt', 'r')
a = f.readline()
m, n = map(int, a.split())
G = [[0]*n for _ in range(n)]
V = []
for _ in range(m):
    a = f.readline()
    v1, v2 = a.split()
    for v in (v1, v2):
        if v not in V:
            V.append(v)
    G[V.index(v1)][V.index(v2)] = 1
    G[V.index(v2)][V.index(v1)] = 1

dist = distance(G)
for i in range(n):
    for j in range(m):
        print(dist[i][j], end='  ')
    print()

radius = min(max(row) for row in dist)
print(f"Радиус графа: {radius}")

diameter = max(max(row) for row in dist)
print(f"Диаметр графа: {diameter}")

center = [i for i, row in enumerate(dist) if max(row) == radius]
print(f"Центр графа: {center}")