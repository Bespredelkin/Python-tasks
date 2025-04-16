def novoe_zveno(value):
    return {'value':value,'next':None}
def sozdanie_spiska(n, head):
    for i in range(n):
        value = int(input())
        current = novoe_zveno(value)
        if head == None:
            head = current
        else:
            prev['next'] = current
        prev = current
    return head

def bum(head, k):
    nachalo = head
    konets = head
    schet = 0
    while konets != None:
        konets = konets['next']
        schet += 1
    for i in range(schet - k):
        nachalo = nachalo['next']
    nachalo["next"] = nachalo
    print("найденый элемент : ", nachalo["value"])
head = None
n = int(input("Введите количество звеньев"))
head = sozdanie_spiska(n, head)
k = int(input('удалите чего хотите'))
bum(head, k)

