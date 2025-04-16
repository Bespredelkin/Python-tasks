from collections import deque
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class Tree:
    def __init__(self):
        self.Root = None

    def ins_node(self, node, value):
        if node.value == value:
            return
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self.ins_node(node.right, value)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.ins_node(node.left, value)

    def ins_tree(self, value):
        if self.Root is None:
            self.Root = Node(value)
        else:
            self.ins_node(self.Root, value)

    def print_tree_simetric(self, node):
        if node is None:
            return
        self.print_tree_simetric(node.left)
        print(node.value, end=' ')
        self.print_tree_simetric(node.right)

    def print_tree_direct(self, node):
        if node is None:
            return
        print(node.value, end=' ')
        self.print_tree_direct(node.left)
        self.print_tree_direct(node.right)

    def print_tree_reverse(self, node):
        if node is None:
            return
        self.print_tree_reverse(node.left)
        self.print_tree_reverse(node.right)
        print(node.value, end=' ')

    def vstavka(self, vstav):
        self.ins_tree(vstav)
        self.print_tree_simetric(self.Root)

    def obhod_v_shirinu(self, node):
        if node is None:
            return
        que = deque()
        que.append(node)
        while len(que) != 0:
            Node = que.popleft()
            if Node.left != None:
                que.append(Node.left)
            if Node.right != None:
                que.append(Node.right)
            print(Node.value, end=" ")

    def udalenie_uzla(self, node, udol):
        if node is None:
            return
        if node.left is not None and node.left.value == udol:
            node.left = None
            return
        if node.right is not None and node.right.value == udol:
            node.right = None
            return
        self.udalenie_uzla(node.left, udol)
        self.udalenie_uzla(node.right, udol)

    def udalenie_element(self, node, udoli):
        if node is None:
            return
        if node.left is not None and node.left.value == udoli:
            if node.left.left.value is None and node.left.right.value is None:
                node.left = None
                return
            if node.left.left.value is None or node.left.right.value is None:
                if node.left.right.value is None:
                    node.left = node.left.left
                    return
                if node.left.left.value is None:
                    node.left = node.left.right
                    return
            else:
                zap = node.left.left
                while zap.right.right != None:
                    zap = zap.right
                if zap.right.left == None:
                    node.left = zap.right
                    zap.right = None
                    return
                else:
                    node.left = zap.right
                    zap = zap.right.left
                    return

        if node.right is not None and node.right.value == udoli:
            if node.right.left.value is None and node.right.right.value is None:
                node.right = None
                return
            if node.right.left.value is None or node.right.right.value is None:
                if node.right.left.value is None:
                    node.right = node.right.right
                    return
                if node.right.right.value is None:
                    node.right = node.right.left
                    return
            else:
                zap = node.right.right
                while zap.left.left != None:
                    zap = zap.left
                if zap.left.right == None:
                    node.right = zap.left
                    zap.left = None
                    return
                else:
                    node.right = zap.left
                    zap = zap.left.right
                    return
        self.udalenie_uzla(node.left, udoli)
        self.udalenie_uzla(node.right, udoli)
    def pustota(self):
        if self.Root is None:
            print("Пустое")
        else:
            print("Не пустое")

    def udalenie_dereva(self):
        self.Root = None
        print(self)

    def dlina(self, node):
        if node is None:
            return 0
        else:
            return max(self.dlina(node.left), self.dlina(node.right)) + 1


t = Tree()
l = list(map(int, input("Введите список").split()))
for i in l:
    t.ins_tree(i)

while 0 == 0:
    print()
    a = int(input("Введите номер команды"))
    if a == 0:
        exit()
    if a == 1:
        t.print_tree_simetric(t.Root)
    if a == 2:
        t.print_tree_reverse(t.Root)
    if a == 3:
        t.print_tree_direct(t.Root)
    if a == 4:
        vstav = int(input("Введите элемент для вставки"))
        t.vstavka(vstav)
    if a == 5:
        udol = int(input("Введите элемент для удаления его дерева"))
        t.udalenie_uzla(t.Root, udol)
        t.print_tree_simetric(t.Root)
    if a == 6:
        t.pustota()
    if a == 7:
        t.udalenie_dereva()
    if a == 8:
        print(t.dlina(t.Root))
    if a == 9:
        udoli = int(input("Введите элемент для удаления"))
        t.udalenie_element(t.Root, udoli)
        t.print_tree_simetric(t.Root)
    if a == 10:
        t.obhod_v_shirinu(t.Root)
