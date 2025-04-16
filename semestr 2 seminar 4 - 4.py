import heapq
kucha = list(input().split())
heap = list(map(int,kucha))
item = int(input())
heapq.heappush(heap,item)
print(heap)