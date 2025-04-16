def RabinKarp(string, p):
    n, m = len(string), len(p)
    hp = hash(p)
    a = ''
    for i in range(n-m+1):
        hs = hash(string[i:i+m])
        if hs == hp:
            if string[i:i+m] == p:
                a = a + str(i) + ' '
        if i == n - m and a != '':
            return a
    return -1
isk = input()
stroka = str(input())
print(RabinKarp(stroka, isk))