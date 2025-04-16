import heapq

N, M, S, F = map(int, input().split())

G = [[] for _ in range(N)]
for _ in range(M):
    u, v, w = map(int, input().split())
    G[u].append((v, w))
    G[v].append((u, w))

dist = [float("inf")] * N
dist[S] = 0
prev = [-1] * N
pop = []
heapq.heappush(pop, (0, S))


while pop:
    currentdist, currentnode = heapq.heappop(pop)
    if currentdist > dist[currentnode]:
        continue
    for neighbor, weight in G[currentnode]:
        newdist = dist[currentnode] + weight
        if newdist < dist[neighbor]:
            dist[neighbor] = newdist
            prev[neighbor] = currentnode
            heapq.heappush(pop, (newdist, neighbor))



if dist[F] == float("inf"):
    print("No path")
else:
    print(dist[F])
    road = []
    current = F
    while current != -1:
        road.append(current)
        current = prev[current]
    print(*reversed(road))
