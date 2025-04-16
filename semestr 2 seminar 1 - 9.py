def f(M, K):
    if M == 1:
        return K
    else:
        return 2 * K + f(M - 1, K + 1)
M = int(input())
K = int(input())
print(f(M, K))