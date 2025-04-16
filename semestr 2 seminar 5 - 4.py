def novoe_zveno(value):
    return {"prev": None, "value": value, "next": None}
def novi_spisoc():
    return {"head": None, "tail": None}
def sozdanie_spiska(n, list):
    for i in range(n):
        value = int(input('Введите звено'))
        current = novoe_zveno(value)
        if list['head'] == None:
            list['head'] = current
            list['tail'] = current
        else:
            prev["next"] = current
            current["prev"] = prev
            list['tail'] = current
        prev = current
    return list
def raspechatka_vpered():
    current = list["head"]
    while current != None:
        print(current["value"], end=' ')
        current = current["next"]
def raspechatka_nazad():
    current = list["tail"]
    while current != None:
        print(current["value"], end=' ')
        current = current["prev"]
def dobavlemie_v_nachalo(list,valdob):
    current = novoe_zveno(valdob)
    current["prev"] = list["head"]
    list["head"] = current
    current["next"] = current["prev"]
    return list
def dobavlemie_v_konets(list, valdob):
    current = list['head']
    while current != None:
        prev = current
        current = current['next']
    current = novoe_zveno(valdob)
    prev['next'] = current
    return list
def dobavlemie_do_zvena(list,valdob, valdo):
    current = list["head"]
    while current['value'] != valdo:
        prev = current
        current = current['next']
    current = novoe_zveno(valdob)
    current['next'] = prev['next']
    prev['next'] = current

    return list
def udalenie_nachala(list):
    current = list["head"]["next"]
    list['head'] = current
    return list
def udalenie_konets(list):
    current = list['head']
    next = list['head']['next']
    while next != None:
        prev = current
        current = next
        next = next['next']
    prev['next'] = None
    return list
def udalenie_zvena(list, valud):
    current = list["head"]
    while current['value'] != valud:
        if current['next'] == None:
            print("value is not available")
            return
        prev = current
        current = current['next']
    prev['next'] = current['next']
    return list

n = int(input("Введите количество звеньев"))
list = novi_spisoc()
sozdanie_spiska(n, list)
while 0 == 0:
    a = int(input("Введите номер команды"))
    if a == 0:
        exit()
    if a == 1:
        raspechatka_vpered()
    if a == 2:
        raspechatka_nazad()
    if a == 3:
        valdob = int(input('Добавте чего хотите'))
        list = dobavlemie_v_nachalo(list, valdob)
        raspechatka_vpered()
    if a == 4:
        valdob = int(input('Добавте чего хотите'))
        list = dobavlemie_v_konets(list, valdob)
        raspechatka_vpered()
    if a == 5:
        valdo = int(input('до какого элемента хотите добавить?'))
        valdob = int(input('Добавте чего хотите'))
        list = dobavlemie_do_zvena(list, valdob, valdo)
        raspechatka_vpered()
    if a == 6:
        list = udalenie_nachala(list)
        raspechatka_vpered()
    if a == 7:
        list = udalenie_konets(list)
        raspechatka_vpered()
    if a == 8:
        valud = int(input('Удалите чего хотите'))
        list = udalenie_zvena(list, valud)
        raspechatka_vpered()
    if a == 9:
        list["head"] = None
        raspechatka_vpered()