from datetime import date

a = date(4098, 4, 3)
b = date(2387, 5, 23)
date_entry = input('Enter a date in YYYY-MM-DD format')
year, month, day = map(int, date_entry.split('-'))
c = date(year,month,day)
if a > c and b > c: print('ниже первой')
elif b < c and a < c: print('выше второй')
else : print('между')
