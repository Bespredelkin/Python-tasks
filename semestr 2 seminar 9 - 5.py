from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


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

    def obhod_v_shirinu(self, node):
        if node is None:
            return
        que = deque()
        que.append(node)
        while len(que) != 0:
            node = que.popleft()
            if node.left != None:
                que.append(node.left)
            if node.right != None:
                que.append(node.right)
            print(node.value, end=" ")

    def zerkalo_node(self, node):
        if node is None:
            return None
        else:
            left = self.zerkalo_node(node.left)
            right = self.zerkalo_node(node.right)
            node.left = right
            node.right = left
            return node

    def zerkalo_tree(self):
        self.zerkalo_node(self.Root)

t = Tree()
l = list(map(int, input("Введите список").split()))
for i in l:
    t.ins_tree(i)

t.zerkalo_tree()
t.obhod_v_shirinu(t.Root)
