def start():
	a = input("Ваши данные: ")
	print("\n\n[int][bin][oct][hex]")
	v = input("Какой это тип: ")
	if v == "bin":
		v = 2
	elif v == "oct":
		v = 8
	elif v == "hex":
		v = 16
	else:
		v = 10
	print("\n\n[int][bin][oct][hex]")
	b = input("В какой тип: ")
	try:
		a = int(a, v)
		if b == "bin":
			a = bin(a)
		elif b == "oct":
			a = oct(a)
		elif b == "hex":
			a = hex(a)
		elif b == "int":
			a = int(a)
		else:
			int("Вызов ValueError")
		return a
	except ValueError:
		print("\n\nДанные не валидны")
		start()

a = start()
print(a)
