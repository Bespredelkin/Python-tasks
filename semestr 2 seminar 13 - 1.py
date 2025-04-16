from pythonds.basic import Stack
G = {}
for line in open('eiler.txt', 'r'):
    v1, v2 = line.split()
    for v in (v1, v2):
        if v not in G:
            G[v] = []
    G[v1].append(v2)
    G[v2].append(v1)
stacki = Stack()
number_nechet_hights = 0
road = []
for i in G:
    if len(G[i]) % 2 != 0:
        number_nechet_hights += 1
        start = i
if number_nechet_hights != 2:
    print('Ты не пройдёшь!')
    quit()
if number_nechet_hights == 0:
    start = number_nechet_hights

stacki.push(start)
while not stacki.isEmpty():
    i = stacki.peek()
    if len(G[i]) == 0:
        road.append(stacki.pop())
    else:
        j = G[i][0]
        G[i].remove(j)
        G[j].remove(i)
        stacki.push(j)
print(road)

