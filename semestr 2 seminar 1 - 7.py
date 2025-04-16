def f(m , n):
    if m==0:
        return n+1
    if n == 0 and m!=0:
        return f(m-1,1)
    else:
        return f(m-1 , f(m,n-1))
m = int(input())
n = int(input())
print(f(m , n))