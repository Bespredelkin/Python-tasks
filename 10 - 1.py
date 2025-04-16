def Myau(n):
    if n == 0 or n == 1: return 1
    else: return Myau(n-1) + Myau(n-2) + 1
print(Myau(int(input())))