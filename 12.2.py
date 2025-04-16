a = 'abbaabbab'
b = 'abbaabbab'
c = 'aabaabaaaabaabаaab'
d = 'liilliil'

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
print(gg(a))
print(gg(b))
print(gg(c))
print(gg(d))