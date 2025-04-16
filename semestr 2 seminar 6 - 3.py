from pythonds.basic import Stack
Stack=Stack()
print(Stack.isEmpty())
for i in range(0,10):
    Stack.push(i)
print(Stack.peek())
print(Stack.size())
print(Stack.isEmpty())
for i in range(0,10):
    print(Stack.pop())
print(Stack.isEmpty())
