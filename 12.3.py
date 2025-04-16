t = str(input())
def gg(x):
    p = [0] * len(x)
    j = 0
    i = 1
    while i < len(x):
        if x[j] == x[i]:
            p[i] = j + 1
            i += 1
            j += 1
        else:
            if j == 0:
                p[i] = 0
                i += 1
            else:
                j = p[j - 1]
    return p
print(gg(t))
p = gg(t)
a = str(input())

def gl(y, t, p):
    m = len(y)
    n = len(t)
    i = 0
    j = 0
    while i < m:
        if y[i] == t[j]:
            i += 1
            j += 1
            if j == m:
                return "образ найден"
        else:
            if j > 0:
                j = p[j - 1]
            else:
                i += 1
    if i == n and j != m:
        return "образ не найден"
print(gl(a, t, p))