print('vvedite binarik')
x=input()
def perevod(y):
    c=0
    a=1
    for i in range(len(y), 0 ,-1):
        if y[i-1]=='1':
            c+=a
        a=a*2
    return c
print(perevod(x))
