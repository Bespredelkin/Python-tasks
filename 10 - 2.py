max=1000000
a = [-1] * max

def b(n):
    if n <= 1:
        return 1
    if a[n] == -1:
        if n % 2 == 0:
            a[n] = b(int(n/2)) + b(int(n/2) - 1)
        else:
            a[n] = b(n//2) - b(n//2 - 1)
    return a[n]
print(b(int(input())))