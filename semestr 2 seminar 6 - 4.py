from pythonds.basic import Stack
a = list(input().split())
Stack=Stack()
b = len(a)
for i in range(0, b):
    Stack.push(a[i])
for i in range(0,b):
    print(Stack.pop(), end=' ')