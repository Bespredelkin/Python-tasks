def function_enter1(kucha):
    element1 = list(map(int, list(input().split())))
    for i in range(len(element1)):
        kucha.append(element1[i])
        rabota1(kucha, len(kucha) - 1)
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
kucha1 = []
kucha2 = []
print(function_enter1(kucha1))
print(function_enter2(kucha2))