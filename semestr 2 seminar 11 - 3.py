file = open('1-11.txt','r')
a = file.read()
b = a.split()
for i in range(len(b)):
    print('-'.join(b[i]))
