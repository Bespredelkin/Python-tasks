def function_enter1(kucha):
    element1 = list(map(int, list(input().split())))
    for i in range(len(element1)):
        kucha.append(element1[i])
        rabota1(kucha, len(kucha) - 1)
    print(kucha)
    return kucha

def rabota1(kucha , index):
    if index == 0:
        return
    if kucha[(index - 1) // 2] >= kucha[index]:
        kucha[(index - 1) // 2], kucha[index] = kucha[index], kucha[(index - 1) // 2]
        rabota1(kucha, (index - 1) // 2)
def function_enter2(kucha):
    element2 = list(map(int, list(input().split())))
    for i in range(len(element2)):
        kucha.append(element2[i])
        rabota2(kucha, len(kucha) - 1)
    return kucha

def rabota2(kucha, index):
    if index == 0:
        return
    if kucha[(index - 1) // 2] <= kucha[index]:
        kucha[(index - 1) // 2], kucha[index] = kucha[index], kucha[(index - 1) // 2]
        rabota2(kucha, (index - 1) // 2)

def function_enter11(kucha):
    stroka = []
    stroka.append(kucha[0])
    for i in range(len(kucha) - 1):
         kucha[0], kucha[len(kucha) - 1] = kucha[len(kucha) - 1], kucha[0]
         kucha.pop()
         rabota11(kucha, 0)
         stroka.append(kucha[0])
    return stroka

def rabota11(kucha, index):
    if index * 2 + 1 > len(kucha) - 1:
        return
    elif index * 2 + 2 > len(kucha) - 1:
        if kucha[index] > kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota11(kucha, index * 2 + 1)
        return
    elif kucha[index] > kucha[index * 2 + 1]:
        kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
        rabota11(kucha, index * 2 + 1)
        if kucha[index] >= kucha[index * 2 + 2]:
            kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
            rabota11(kucha, index * 2 + 2)
        return
    elif kucha[index] >= kucha[index * 2 + 2]:
        kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
        rabota11(kucha, index * 2 + 2)
        if kucha[index] >= kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota11(kucha, index * 2 + 1)
        return

def function_enter22(kucha):
    stroka = []
    stroka.append(kucha[0])
    for i in range(len(kucha) - 1):
         kucha[0], kucha[len(kucha) - 1] = kucha[len(kucha) - 1], kucha[0]
         kucha.pop()
         rabota22(kucha, 0)
         stroka.append(kucha[0])
    return stroka

def rabota22(kucha, index):
    if index * 2 + 1 > len(kucha) - 1:
        return
    elif index * 2 + 2 > len(kucha) - 1:
        if kucha[index] < kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota22(kucha, index * 2 + 1)
        return
    elif kucha[index] < kucha[index * 2 + 1]:
        kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
        rabota22(kucha, index * 2 + 1)
        if kucha[index] < kucha[index * 2 + 2]:
            kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
            rabota22(kucha, index * 2 + 2)
        return
    elif kucha[index] <= kucha[index * 2 + 2]:
        kucha[index], kucha[index * 2 + 2] = kucha[index * 2 + 2], kucha[index]
        rabota22(kucha, index * 2 + 2)
        if kucha[index] <= kucha[index * 2 + 1]:
            kucha[index], kucha[index * 2 + 1] = kucha[index * 2 + 1], kucha[index]
            rabota22(kucha, index * 2 + 1)
        return

kucha1 = []
kucha2 = []
print(function_enter11(function_enter1(kucha1)))
print(function_enter22(function_enter2(kucha2)))