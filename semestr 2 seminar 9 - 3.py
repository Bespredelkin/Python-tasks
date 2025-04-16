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
            node.right = Node(value)
        elif value > node.value:
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

    def simmetria(self, left, right):
        if self.Root is None:
            return True
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.value != right.value:
            return False
        else:
            return self.simmetria(left.left, right.right) and self.simmetria(left.right, right.left)



t = Tree()
l = list(map(int, input("Введите список").split()))
for i in l:
    t.ins_tree(i)

print(t.simmetria(t.Root.left, t.Root.right))