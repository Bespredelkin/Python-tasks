import heapq
kuchap = list(input('Введите список для кучи').split())
kucha1 = list(map(int, kuchap))
item = int(input('элемент для добавления'))
n = int(input('количество возращаемых элементов'))
a = heapq.heapreplace(kucha1, item)
b = heapq.heappushpop(kucha1, item)
c = heapq.nlargest(n, kucha1, key=None)
d = heapq.nsmallest(n, kucha1, key=None)
print(a)
print(b)
print(c)
print(d)