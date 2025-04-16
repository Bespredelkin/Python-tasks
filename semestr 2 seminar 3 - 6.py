dictionary_1 = {'a': 300, 'b': 400}
dictionary_1.update({'g' : 5})
print(dictionary_1)
dictionary_1.setdefault('v', 6)
dictionary_1.setdefault('b', 6)
print(dictionary_1)