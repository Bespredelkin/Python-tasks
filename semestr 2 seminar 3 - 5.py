def ya_function(a , b):
    return b.get(a, 'нету')
a = 7
b = {1 : 'a' , 2 : 'b' , 3 : 'c' , 4 : 'd'}
print(ya_function(a , b))