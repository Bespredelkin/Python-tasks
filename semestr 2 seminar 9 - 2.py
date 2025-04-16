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
def dlina(node):
    if node is None:
        return 0
    else:
        return max(dlina(node['left']), dlina(node['right'])) + 1
def sravnenie(node):
    if node is None:
        return 0
    if abs(dlina(node['left']) - dlina(node['right'])) <= 1:
        print("Сбалансированное")
    else:
        print("не сбалансированое")

t = tree()
l = list(map(int, input("Введите список").split()))
for i in l:
    ins_tree(t, i)

sravnenie(t['Root'])



