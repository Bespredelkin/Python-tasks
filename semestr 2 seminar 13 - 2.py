def dfs(node, visited, G):
    if visited is None:
        visited = set()
    visited.add(node)
    for neighbor in G[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, G)
G = {}
for line in open('svas.txt', 'r'):
    v1, v2 = line.split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)
visited = set()
count = 0

for i in G.keys():
    if i not in visited:
        count += 1
        dfs(i, visited, G)
print(count)