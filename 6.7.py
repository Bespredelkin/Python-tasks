print('введите посл')
a = list(map(int, input().split()))
ln = 1
maxln = 1
maxind = 0
b = []
for i in range(1, len(a)-1):
    if a[i] - a[i - 1] == a[i + 1] - a[i]:
        ln += 1
        if ln >= maxln:
            maxln = ln
            maxind = i - ln + 1
    else:
        ln = 1
if len(a) == 0:
    print('0')
elif len(a) == 1:
    print('1')
else:
    print(maxln + 1)

for i in range(maxind , maxind + maxln + 1):
    b.append(a[i])
print(b)