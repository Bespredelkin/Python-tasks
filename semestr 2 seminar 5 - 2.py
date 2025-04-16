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

def sortirovka(head):
    if head == None:
        return
    current = head
    while current != None:
        i = current["next"]
        while i != None:
            if current["value"] > i["value"]:
                i["value"], current["value"] = current["value"], i["value"]
            i = i["next"]
        current = current["next"]
    raspechatka()

head = None
n = int(input("Введите количество звеньев"))
head = sozdanie_spiska(n, head)
sortirovka(head)