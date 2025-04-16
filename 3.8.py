print('vvedite integer')
x=int(input())
a=bin(x)
def perevod(x):
    y=''
    while x > 0:
        if x % 2:
            y = y + '1'
        else: y = y + '0'
        x = x // 2
    return y

def invert(s):
    y = '0b'
    for i in range(len(s), 0 , -1):
        y += s[i-1]
    return y
g=invert(perevod(x))
print(a)
print(g)
if a==g: print('true')