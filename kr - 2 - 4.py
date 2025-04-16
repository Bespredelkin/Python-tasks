import datetime
a = [4,43,45,4,53,4,534,5,2,5,35,34,5,345,34,5,3,53,5,345,3,45,3,5,345,34,5,345,3,45,345,3,5,345,2,5,35,3,45,345,34,5,345,34,25,345,346,6,767,8,678,56,7,6,4,6,23,4,234,23,42,34,234,2,4,24,23,42,4,2,42,4,1,43,4,2,34]
start_time = datetime.datetime.now()
#Метод пузырька
def pusir(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a
print(pusir(a))
print("t1=",datetime.datetime.now() - start_time)
start_time = datetime.datetime.now()
#Метод простого выбора
def vibor(a):
    for i in range(0, len(a) - 1):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a
print(vibor(a))
print("t2=",datetime.datetime.now() - start_time)
start_time = datetime.datetime.now()
#Метод простой вставки
def vstavka(a):
    for i in range(1, len(a)):
        temp = a[i]
        j = i - 1
        while j >= 0 and temp < a[j]:
            a[j + 1] = a[j]
            j = j - 1
        a[j + 1] = temp
    return a
print(vstavka(a))
print("t3=",datetime.datetime.now() - start_time)

