from collections import deque
def read_graph(filename):
    n = None
    G = {}
    for a in open(filename, 'r'):
        if n is None:
            n, m = map(int, a.split())
            continue
        v1, v2 = a.split()
        for v in (v1, v2):
            if v not in G:
                G[v] = []
        G[v1].append(v2)
        G[v2].append(v1)
    return G

def bfs(G, node, visited = None):
    global N
    if visited is None:
        visited = set()
    q = deque()
    q.append(node)
    while q:
        current = q.popleft()
        if current not in visited:
            N += 1
            visited.add(current)
            print('{} is {} vertex'.format(current, N))
            for neig in G[current]:
                q.append(neig)

G = read_graph('12-1.txt')
N = 0
visited = set()
for node in G.keys():
    if node not in visited:
        bfs(G,node, visited)