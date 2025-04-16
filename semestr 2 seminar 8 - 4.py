s = str(input())
M = int(input())
def hash1(s, M):
    h = 0
    for c in s:
        h = (h+ ord(c)) % M
    return h
print(hash1(s,M))