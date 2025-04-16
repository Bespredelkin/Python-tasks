import heapq
kuchap = list(input('Введите список для кучи').split())
kucha1 = list(map(int,kuchap))
kuchap = list(input('Введите список для кучи').split())
kucha2 = list(map(int,kuchap))
a = list(heapq.merge(kucha1 , kucha2 , key = None , reverse = False))
print(a)