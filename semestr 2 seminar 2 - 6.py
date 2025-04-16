a = input()
last = []
while a != '':
    last.append(a)
    a = input()
else:
    print(list(set(last)))