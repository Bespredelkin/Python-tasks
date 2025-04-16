from collections import deque
que = deque()
for i in range(10):
    que.append(i)
print(que)
for i in range(10):
    que.appendleft(i)
print(que)
for i in range(5):
    que.pop()
print(que)
for i in range(5):
    que.popleft()
print(que)
print(que.index(4))
que.insert(2, 1000)
print(que)
que.remove(0)
print(que)
print(que.count(5))
que.extend([100])
print(que)
que.extendleft([100])
print(que)
que.reverse()
print(que)
que.rotate(5)
print(que)
