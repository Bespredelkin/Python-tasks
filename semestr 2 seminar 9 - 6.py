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

    def predki(self, node, ud):
        a = []
        if node is None:
            return
        current = node
        while current.value != ud:
            a.append(current.value)
            if current.value > ud:
                current = current.left
            else:
                current = current.right
            if current is None:
                return a
        return a


t = Tree()
l = list(map(int, input("Введите список").split()))
for i in l:
    t.ins_tree(i)

ud = int(input())
print(t.predki(t.Root, ud))