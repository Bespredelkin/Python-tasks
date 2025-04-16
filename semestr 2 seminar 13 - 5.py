from queue import Queue
G = {}
for line in open('13-4.txt', 'r'):
    v1, v2 = line.split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)

def bfs(G, start):
    interval = {i: None for i in G}
    q = Queue()
    q.put(start)
    interval[start] = 0
    while not q.empty():
        i = q.get()
        for neighbour in G[i]:
            if interval[neighbour] == None:
                q.put(neighbour)
                interval[neighbour] = interval[i] + 1
    return interval


def road(G, start, end):
    distance = bfs(G, start)
    res = [end]
    while distance[end] != 0:
        for v in G[end]: # соседи вершины end
            if distance[end] - distance[v] == 1:
                end = v
                res.append(end)
                break
    return res[::-1]

while 0 == 0:
    a = int(input('Выйдете или найдите минимальный путь'))
    if a == 0:
        exit()
    if a == 1:
        start = input('Введите начальный узел')
        end = input('Введите начальный узел')
        print(road(G, start, end))
