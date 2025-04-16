print('vvedite integer')
x=int(input())
def perevod(x):
    y=0
    while x > 0:
        if x % 2:
            y = y + 1
        x = x // 2
    return y
print(perevod(x))
print(1)