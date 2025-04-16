def function_enter1(kucha,element):
    kucha.append(element)
    rabota1(kucha, len(kucha) - 1)
    return kucha
def rabota1(kucha , index):
    if index == 0:
        return
    if kucha[(index - 1) // 2] >= kucha[index]:
        kucha[(index - 1) // 2], kucha[index] = kucha[index], kucha[(index - 1) // 2]
        rabota1(kucha, (index - 1) // 2)
def function_enter2(kucha, element):
    kucha.append(element)
    rabota2(kucha, len(kucha) - 1)
    return kucha
def rabota2(kucha, index):
    if index == 0:
        return
    if kucha[(index - 1) // 2] <= kucha[index]:
        kucha[(index - 1) // 2], kucha[index] = kucha[index], kucha[(index - 1) // 2]
        rabota2(kucha, (index - 1) // 2)





kucha1 = [1,2,3,4,5]
element1 = int(input())
kucha2 = [5,4,3,2,1]
element2 = int(input())
print(kucha1)
print(kucha2)
print(function_enter1(kucha1,element1))
print(function_enter2(kucha2,element2))