import heapq
kucha = list(input().split())
heap = list(map(int,kucha))
heapq.heapify(heap)
print(heap)