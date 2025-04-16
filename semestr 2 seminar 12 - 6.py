f = open('12-1.txt', 'r')
a = f.readline()
G = {}
m, n = map(int, a.split())
for _ in range(m):
    a = f.readline()
    v1, v2 = a.split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)

def dfs(G, node, visited = None):
    if visited is None:
        visited = set()
    visited.add(node)
    print('{} call'.format(node))
    for neighbor in G[node]:
        if neighbor not in visited:
            dfs(G, neighbor, visited)
    print('{} end'.format(node))
dfs(G, 'A')