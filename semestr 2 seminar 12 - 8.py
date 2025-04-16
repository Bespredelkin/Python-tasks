'''Контест по графам для начинающих'''


'''Задача 1'''

from collections import deque
n, m = map(int, input().split())
G = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [float('inf') for _ in range(n)]
dist[0] = 0
queue = deque([0])

while queue:
    current = queue.popleft()
    for neighbor in G[current]:
        if dist[neighbor] == float('inf'):
            dist[neighbor] = dist[current] + 1
            queue.append(neighbor)

for d in dist:
    print(d)

'''Задача 2'''

def dfs(node, visited, G):
    visited[node] = True
    for neighbor in G[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, G)

n = int(input())
m = int(input())

G = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

visited = [False] * n
count = 0

for i in range(n):
    if not visited[i]:
        count += 1
        dfs(i, visited, G)

print(count)

'''Задача 3'''

def dfs(G, visited, node):
    visited[node] = True
    for neighbor in G[node]:
        if not visited[neighbor]:
            dfs(G, visited, neighbor)


n, m = map(int, input().split())
visited = [False] * n
v_values = []
G = [[] for i in range(n)]

for i in range(m):
    v_values.append(list(map(int, input().split())))

for v in v_values:
    if v[1] not in G[v[0]]:
        G[v[0]].append(v[1])
    if v[0] not in G[v[1]]:
        G[v[1]].append(v[0])

svas = []

for i in range(n):
    if not visited[i]:
        before = [i for i in visited]
        dfs(G, visited, i)
        after = [i for i in visited]
        svas.append([])
        for j in range(n):
            if after[j] and not before[j]:
                svas[-1].append(j)

G_massa = [0 for i in range(n)]

for v in v_values:
    G_massa[v[0]] += v[2]
    G_massa[v[1]] += v[2]

svas_massa = []

for k in svas:
    massa = 0
    for i in k:
        massa += G_massa[i] / 2
    svas_massa.append(int(massa))

svas_massa.sort()

for i in svas_massa:
    print(i)

'''Задача 4'''

def dfs(G, node, visited, stack, cycle):
    visited[node] = True
    cycle[node] = True
    for neighbor in G[node]:
        if cycle[neighbor]:
            return True
        if not visited[neighbor]:
            if dfs(G, neighbor, visited, stack, cycle):
                return True

    cycle[node] = False
    stack.append(node)
    return False

def topological(G, vertices):
    visited = [False] * vertices
    stack = []
    cycle = [False] * vertices

    for i in range(vertices):
        if not visited[i]:
            if dfs(G, i, visited, stack, cycle):
                return "NO"

    return reversed(stack)

n, m = map(int, input().split())
G = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)

result = topological(G, n)

if result == "NO":
    print("NO")
else:
    print(*result)