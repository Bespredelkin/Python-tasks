from datetime import datetime
start_time = datetime.now()
a = 'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLALALLALALLALALALLALALALALALALALALALALALALALALALALALALALALAL'
b = "LALALALALA"
c = -1
j = 0
i = 0
while i <= len(b) - 1:
	while j <= len(a) - 1:
		if b[i] == a[j]:
			c = j
			j += 1
			i += 1
			if i == len(b) - 1 and c != -1:
				print(c + 1)
				print(datetime.now() - start_time)
				quit()

		elif j == len(a) - 1:
			print(datetime.now() - start_time)
			print('NO')
			quit()
		else:
			i = 0
			c = -1
