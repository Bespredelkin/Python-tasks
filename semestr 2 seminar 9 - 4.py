from collections import deque
class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.summ = value


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

        node.summ = node.value
        if node.left:
            node.summ += node.left.summ
        if node.right:
            node.summ += node.right.summ

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
        i = 0
        while len(que) != 0:
            Node = que.popleft()
            if i < 3:
                print(Node.summ, end=" ")
            if Node.left != None:
                que.append(Node.left)
            if Node.right != None:
                que.append(Node.right)
            if i >= 3:
                print(0, end=" ")
            i += 1


t = Tree()
l = list(map(int, input("Введите список").split()))
for i in l:
    t.ins_tree(i)

t.obhod_v_shirinu(t.Root)

