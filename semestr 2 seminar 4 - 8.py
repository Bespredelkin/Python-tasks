def function_enter1(kucha):
    stroka = []
    stroka.append(kucha[0])
    for i in range(len(kucha) - 1):
         kucha[0], kucha[len(kucha) - 1] = kucha[len(kucha) - 1], kucha[0]
         kucha.pop()
         rabota1(kucha, 0)
         stroka.append(kucha[0])
    return stroka
def rabota1(kucha, index):
    if index * 2 + 1 > len(kucha) - 1:
        return
    elif index * 2 + 2 > len(kucha) - 1:
        if kucha[index] > kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota1(kucha, index * 2 + 1)
        return
    elif kucha[index] > kucha[index * 2 + 1]:
        kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
        rabota1(kucha, index * 2 + 1)
        if kucha[index] >= kucha[index * 2 + 2]:
            kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
            rabota1(kucha, index * 2 + 2)
        return
    elif kucha[index] >= kucha[index * 2 + 2]:
        kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
        rabota1(kucha, index * 2 + 2)
        if kucha[index] >= kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota1(kucha, index * 2 + 1)
        return

def function_enter2(kucha):
    stroka = []
    stroka.append(kucha[0])
    for i in range(len(kucha) - 1):
         kucha[0], kucha[len(kucha) - 1] = kucha[len(kucha) - 1], kucha[0]
         kucha.pop()
         rabota2(kucha, 0)
         stroka.append(kucha[0])
    return stroka
def rabota2(kucha, index):
    if index * 2 + 1 > len(kucha) - 1:
        return
    elif index * 2 + 2 > len(kucha) - 1:
        if kucha[index] < kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota2(kucha, index * 2 + 1)
        return
    elif kucha[index] < kucha[index * 2 + 1]:
        kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
        rabota2(kucha, index * 2 + 1)
        if kucha[index] < kucha[index * 2 + 2]:
            kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
            rabota2(kucha, index * 2 + 2)
        return
    elif kucha[index] <= kucha[index * 2 + 2]:
        kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
        rabota2(kucha, index * 2 + 2)
        if kucha[index] <= kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota2(kucha, index * 2 + 1)
        return

kuchap = list(input('Введите список для мин кучи').split())
kucha1 = list(map(int,kuchap))
kuchap = list(input('Введите список для макс кучи').split())
kucha2 = list(map(int,kuchap))
print(function_enter1(kucha1))
print(function_enter2(kucha2))