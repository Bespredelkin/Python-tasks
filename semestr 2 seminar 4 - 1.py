def rabota1(kucha):
    for index in range(len(kucha) - 1, -1, -1):
        if index == 0:
            return 'kucha'
        elif kucha[(index - 1) // 2] >= kucha[index]:
            print('ne kucha')
            quit()
kuchap = list(input().split())
kucha = list(map(int,kuchap))
print(kucha)
print(rabota1(kucha))

