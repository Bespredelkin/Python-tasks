st1 = input().split()
st2 = input().split()
a = ''
for i in range(0,len(st1)-1):
    if 2 <= i <= 4:
        a += st1[i]
for i in range(0,len(st2)-1):
    if 5 <= i <= 7:
        a += st2[i]
print(a)