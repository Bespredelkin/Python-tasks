from collections import deque
que1 = deque()
que2 = deque()
a = list(map(int,input().split()))
c = []
d=''
for i in range(len(a)):
    if a[i] % 2 != 0:
        que1.append(a[i])
    else:
        que2.append(a[i])
for i in range(len(a)):
    if len(que1) != 0 and len(que2) != 0:
        c.append(que2.pop())
        c.append(que1.pop())
    else:
        break
while len(que1) != 0:
    c.append(que1.pop())
while len(que2) != 0:
    c.append(que2.pop())
for i in range(len(c)):
    d += str(c[i])
    d += ' '
print(d)







