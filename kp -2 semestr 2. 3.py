def no_friends(N, S, Otn):
    number_drugi = 0
    visited = [False] * N
    spis = [S]
    visited[S] = True


    while spis:
        current = spis.pop(0)
        number_drugi += 1
        for drug in Otn[current]:
            if not visited[drug]:
                visited[drug] = True
                spis.append(drug)
    return number_drugi


N, S = map(int, input().split())

prebavka_drusei = []

for _ in range(N):
    prebavka_drusei.append(list(map(int, input().split())))

drugi = [set() for _ in range(N)]

for u in range(N):
    for v in range(N):
        if prebavka_drusei[u][v] == 1:
            drugi[u].add(v)

print(no_friends(N, S, drugi))
