p, M = map(int, input().split())
s = str(input())
def hash1(s, p, M):
    h = 0
    for c in s:
        h = (h*p + ord(c)) % M
    return h
print(hash1(s,p,M))