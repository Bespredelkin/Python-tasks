def novoe_zveno(value):
    return {"value": value, "next": None}
def sozdanie_spiska(n, head):
    for i in range(n):
        value = int(input('Введите звено'))
        current = novoe_zveno(value)
        if head == None:
            head = current
        else:
            prev["next"] = current
        prev = current
    return head
def raspechatka():
    current = head
    while current != None:
        print(current["value"], end=' ')
        current = current["next"]
def dobavlemie_v_nachalo(head,valdob):
    current = novoe_zveno(valdob)
    prev = head
    head = current
    current["next"] = prev
    return head
def dobavlemie_v_konets(head, valdob):
    current = head
    while current != None:
        prev = current
        current = current['next']
    current = novoe_zveno(valdob)
    prev['next'] = current
    return head
def dobavlemie_do_zvena(head,valdob, valdo):
    current = head
    while current['value'] != valdo:
        prev = current
        current = current['next']
    current = novoe_zveno(valdob)
    current['next'] = prev['next']
    prev['next'] = current

    return head
def udalenie_nachala(head):
    current = head['next']
    head = current
    return head
def udalenie_konets(head):
    current = head
    next = head['next']
    while next != None:
        prev = current
        current = next
        next = next['next']
    prev['next'] = None
    return head
def udalenie_zvena(head, valud):
    current = head
    while current['value'] != valud:
        if current['next'] == None:
            print("value is not available")
            return
        prev = current
        current = current['next']
    prev['next'] = current['next']
    return head

head = None
n = int(input("Введите количество звеньев"))
head = sozdanie_spiska(n, head)
while 0 == 0:
    a = int(input("Введите номер команды"))
    if a == 0:
        exit()
    if a == 1:
       head = head
    if a == 2:
        valdob = int(input('Добавте чего хотите'))
        head = dobavlemie_v_nachalo(head, valdob)
    if a == 3:
        valdob = int(input('Добавте чего хотите'))
        head = dobavlemie_v_konets(head, valdob)
    if a == 4:
        valdo = int(input('до какого элемента хотите добавить?'))
        valdob = int(input('Добавте чего хотите'))
        head = dobavlemie_do_zvena(head, valdob, valdo)
    if a == 5:
        head = udalenie_nachala(head)
    if a == 6:
        head = udalenie_konets(head)
    if a == 7:
        valud = int(input('Удалите чего хотите'))
        head = udalenie_zvena(head, valud)
    if a == 8:
        head = None
    raspechatka()