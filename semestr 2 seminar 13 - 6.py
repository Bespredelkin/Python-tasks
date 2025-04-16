from queue import Queue

m = n = None
G = {}
for a in open('13-6.txt', 'r'):
    if n is None:
        n, m = map(int, a.split())
        continue
    v1, v2 = a.split()
    for v in (v1, v2):
        if v not in G:
             G[v] = set()
    G[v1].add(v2)
    G[v2].add(v1)



def bfs(G, start):
    interval = {i: None for i in G}
    q = Queue()
    q.put(start)
    interval[start] = [start]
    while not q.empty():
        i = q.get()
        for neighbour in G[i]:
            if interval[neighbour] == None:
                q.put(neighbour)
                interval[neighbour] = interval[i] + [neighbour]
    return interval

while 0 == 0:
    a = int(input('Выйдете или найдите минимальный путь'))
    if a == 0:
        exit()
    if a == 1:
        Vert = input('Введите начальную вершину')
        print(bfs(G, Vert))