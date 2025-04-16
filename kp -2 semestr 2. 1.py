n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]

stepen = [0] * n
for a, b in edge:
    stepen[a] += 1
    stepen[b] += 1

if all(stepen[i] == stepen[0] for i in range(1, n)):
    print("YES")
else:
    print("NO")
