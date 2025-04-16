n, m = map(int, input().split())
stu = [-1] * n
q = []
G = [[] for _ in range(n)]
for _ in range(m):
    vv, uu = map(int, input().split())
    v, u = vv - 1, uu - 1
    G[v].append(u)
    G[u].append(v)

for i in range(n):
    if stu[i] == -1:
        stu[i] = 0
        q.append(i)
        while q:
            v = q.pop(0)
            for o in G[v]:
                if stu[o] == -1:
                    stu[o] = 1 - stu[v]
                    q.append(o)
                elif stu[o] == stu[v]:
                    print("NO")
                    quit()

print("YES")
for i in range(n):
    if stu[i] == 0:
        print(i + 1, end=" ")
print()



