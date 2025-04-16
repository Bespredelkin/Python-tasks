class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def plusiki(self, a):
        b = len(a)
        for i in range(0, b):
            if a[i] == '+':
                c = int(Stack.pop())
                d = int(Stack.pop())
                e = d + c
                Stack.push(e)

            elif a[i] == '*':
                c = int(Stack.pop())
                d = int(Stack.pop())
                e = d * c
                Stack.push(e)

            elif a[i] == '-':
                c = int(Stack.pop())
                d = int(Stack.pop())
                e = d - c
                Stack.push(e)

            elif a[i] == '/':
                c = int(Stack.pop())
                d = int(Stack.pop())
                e = d / c
                Stack.push(e)

            elif a[i] == '^':
                c = int(Stack.pop())
                d = int(Stack.pop())
                e = d ** c
                Stack.push(e)

            else:
                Stack.push(a[i])

        return Stack.pop()


Stack = Stack()
a = list(input().split())
print(Stack.plusiki(a))