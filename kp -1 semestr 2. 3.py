from collections import deque
que = deque()
a = list(input().split())
for i in range(len(a)):
    que.append(a[i])
for a in range(len(a)//2):
    if que.popleft() != que.pop():
        print('No')
        exit()
print('Yes')