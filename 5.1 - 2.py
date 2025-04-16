class Tree:
    '''дерево представляете??!!'''
    color = 'green'
    def __init__ (self , age , type , country, a):
        self.age = age
        self.type = type
        self.country = country
        self.a = a
    def free(self , age , type , country ,a):
        a = int(a)
        print(" {0}, {1} ".format('Возраст дерева равен ', age))
        print(" {0}, {1} ".format('Данное дерево произрастает в стране ', country))
        if age < 10:
            type = 'fruit'
        else:
            type = 'nonfruit'
        if type == 'fruit':
            a = 1
            return a
        elif type  == 'nonfruit':
            a = 0
            return a
class Fruit(Tree):
    '''Урожай'''
    def __init__ (self, crop ,type):
        super().__init__(self, type)
        self.crop = crop
    def crope(self, crop):
            print(" {0}, {1} ".format('Количество урожая равно ', crop))

class NonFruit(Tree):
    '''Древесина'''
    def __init__ (self, age, wood):
        super().__init__(self, age)
        self.wood = wood
    def woode(self, wood):
            print(" {0}, {1} ".format('Количество древесины равно ', wood))


a = 0
print('введите возраст дерева')
age = input()
type = ''
print('введите страну дерева')
country = input()
crop = 10
wood = 100
opred = Tree(age , type , country ,a)
opred.free(opred.age , opred.type , opred.country , a)
oprede = Fruit(age, crop)
oprede.crope(crop)
opredee = NonFruit(age, wood)
opredee.woode(wood)
if a == 0:
    print("Урожай: ", oprede.crope())
else:
    print("Дерево: ", opredee.woode())




