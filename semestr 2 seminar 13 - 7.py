G = {}
for line in open('13-4.txt', 'r'):
    v1, v2 = line.split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)

def bfs(G, start, end):
    queue = [(start, [start])]
    while queue:
        (node, road) = queue.pop(0)
        for neighbor in G[node]:
            if neighbor not in road:
                if neighbor == end:
                    return True
                else:
                    queue.append((neighbor, road + [neighbor]))
    return False

while 0 == 0:
    a = int(input('Выйдете или проверте достижимость'))
    if a == 0:
        exit()
    if a == 1:
        start = input('Введите начальный узел')
        end = input('Введите начальный узел')
        if bfs(G, start, end):
            print(f"{end} достижим из {start}")
        else:
            print(f"{end} недостежим из {start}")