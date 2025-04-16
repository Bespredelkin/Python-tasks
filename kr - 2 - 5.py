def kont(N):
   # N+=1
    k=[0]*(N+1)
    if N == 1:
        return 2
    elif N == 2:
        return 4
    elif N == 3:
        return 7
    else:
        k[1] = 2
        k[2] = 4
        k[3] = 7
        for i in range(4,N+1):
            k[i] = k[i-1] + k[i-2] + k[i-3]
    return k[N]

N=int(input())
print (kont(N))