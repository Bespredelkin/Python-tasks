import random
a = [random.randrange(1,10,1) for i in range(100)]
dictic = {i: a.count(i) for i in a}
print(a)
print(dictic)