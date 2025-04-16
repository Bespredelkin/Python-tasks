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