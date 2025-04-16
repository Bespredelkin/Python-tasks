def dfs(node, visited, G, stack):
    visited.add(node)
    for neighbor in G[node]:
        if neighbor not in visited:
            dfs(neighbor, visited, G, stack)
        stack.append(node)
G = {}
G_rev = {}
for line in open('Cassorayu.txt', 'r'):
    v1, v2 = line.split()
    for neighbor in (v1, v2):
        if neighbor not in G:
            G[neighbor] = []
            G_rev[neighbor] = []
    G[v1].append(v2)
    G_rev[v2].append(v1)

stack = []
visited = set()
for node in G.keys():
    if node not in visited:
        dfs(node, visited, G, stack)
print(stack)
number = 0
visited = set()
while len(stack) > 0:
    stack_svas = []
    neighbor = stack.pop()
    if neighbor not in visited:
        dfs(neighbor, visited, G_rev, stack_svas)
        number += 1
        print(stack_svas)
print(number)