max = 1000000
a = [1, 1, 2] + [-1] * max
def b(n):
    if a[n] == -1:
        a[n] = b(n - 1) + b(n - 2) + b(n - 3)
    return a[n]
n = int(input())
print(b(n))
