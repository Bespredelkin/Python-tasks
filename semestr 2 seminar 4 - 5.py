import heapq
kucha = list(input().split())
heap = list(map(int,kucha))
heapq.heappop(heap)
print(heap)