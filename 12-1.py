print("введите строку")
a = str(input())
print("введите подстроку")
b = str(input())
c = -1
j = 0
i = 0
while i <= len(b) - 1:
	while j <= len(a) - 1:
		if b[i] == a[j]:
			c = j
			j += 1
			i += 1
			if j == len(b) - 1 and c != -1:
				print(c + 1)
				quit()

		elif i <= len(a) - 1 and c == -1:
			print('NO')
			quit()
		else:
			i = 0
			c = -1

