class Stack:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def get(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def print_stack(self):
        a = len(self.items)
        for i in range(0,a):
            print(self.items.pop())

Stack = Stack()
print(Stack.isEmpty())
for i in range(0,10):
    Stack.push(i)
print(Stack.pop())
print(Stack.get())
print(Stack.size())
Stack.print_stack()
