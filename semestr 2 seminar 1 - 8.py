def matryoshka(i):
    if i == 1:
        return ' matryoshechka ' + str(i)
    if i == 2:
        return ' verc matryoshki ' + str(i) + ' matryoshechka ' + str(i-1) + ' niz matryoshki ' + str(i)
    else:
        return ' verc matryoshki ' + str(i) + matryoshka(i-1) + ' niz matryoshki ' + str(i)

i = int(input())
print(matryoshka(i))






























