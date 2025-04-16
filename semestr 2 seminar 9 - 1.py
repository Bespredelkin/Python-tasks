def tree():
    return {'Root': None}

def Node(value):
    return {'left': None, 'right': None, 'value': value}

def ins_tree(t,value):
    if t['Root'] is None:
        t['Root'] = Node(value)
    else:
        ins_Node(t['Root'], value)
        return

def ins_Node(node, value):
    if node['value'] == value:
        return
    if value > node['value']:
        if node['right'] is None:
            node['right'] = Node(value)
        else:
            ins_Node(node['right'], value)
    elif value < node['value']:
        if node['left'] is None:
            node['left'] = Node(value)
        else:
            ins_Node(node['left'], value)

def print_tree_simetric(node):
     if node is None:
         return
     print_tree_simetric(node['left'])
     print(node['value'], end=' ')
     print_tree_simetric(node['right'])

def print_tree_direct(node):
    if node is None:
        return
    print(node['value'], end=' ')
    print_tree_direct(node['left'])
    print_tree_direct(node['right'])

def print_tree_reverse(node):
    if node is None:
        return
    print_tree_reverse(node['left'])
    print_tree_reverse(node['right'])
    print(node['value'], end=' ')

def vstavka(vstav):
    ins_tree(t, vstav)
    print_tree_simetric(t['Root'])

def udalenie_uzla(node, udol):
    if node is None:
        return
    if node['left'] != None and node['left']['value'] == udol:
        node['left'] = None
        return
    if node['right'] != None and node['right']['value'] == udol:
        node['right'] = None
        return
    udalenie_uzla(node['left'], udol)
    udalenie_uzla(node['right'], udol)

def pustota():
    if t['Root'] == None:
        print("Пустое")
    else:
        print("Не пустое")

def udalenie_dereva():
    t['Root'] = None
    print(t)

def dlina(node):
    if node is None:
        return 0
    else:
        return max(dlina(node['left']), dlina(node['right'])) + 1


t = tree()
l = list(map(int, input("Введите список").split()))
for i in l:
    ins_tree(t, i)

while 0 == 0:
    print()
    a = int(input("Введите номер команды"))
    if a == 0:
        exit()
    if a == 1:
        print_tree_simetric(t['Root'])
    if a == 2:
        print_tree_reverse(t['Root'])
    if a == 3:
        print_tree_direct(t['Root'])
    if a == 4:
        vstav = int(input("Введите элемент для вставки"))
        vstavka(vstav)
    if a == 5:
        udol = int(input("Введите элемент для удаления его дерева"))
        udalenie_uzla(t['Root'], udol)
        print_tree_simetric(t['Root'])
    if a == 6:
        pustota()
    if a == 7:
        udalenie_dereva()
    if a == 8:
        print(dlina(t['Root']))
