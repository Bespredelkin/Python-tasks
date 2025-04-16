class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def scobochki(self, a):
        b = len(a)
        otcrit = ['(', '[', '{']
        zacrit = [')', ']', '}']
        for i in range(0, b):
            for j in range(0,2):
                if a[i] == otcrit[j]:
                    Stack.push(otcrit[j])
            if a[i] == zacrit[0]:
                if Stack.size() == 0:
                    print('False')
                    exit()
                if Stack.pop() != otcrit[0]:
                    print('False')
                    exit()
            elif a[i] == zacrit[1]:
                if Stack.size() == 0:
                    print('False')
                    exit()
                if Stack.pop() != otcrit[1]:
                    print('False')
                    exit()
            elif a[i] == zacrit[2]:
                if Stack.size() == 0:
                    print('False')
                    exit()
                if Stack.pop() != otcrit[2]:
                    print('False')
                    exit()
        if Stack.size() != 0:
            print('False')
            exit()
        else:
            print('True')
Stack = Stack()
a = input()
Stack.scobochki(a)