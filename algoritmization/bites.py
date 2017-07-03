def main():
	in_number = input("Введите число: ")
	try:
		do(int(in_number))
	except ValueError:
		print(in_number + " : недопустимое значение!")
		main()

def do(y):
	x = int(y * "1", 2)
	logical = input("Знаковое ли число? д/н ").lower()
	if logical == "д":
		print(x)
	elif logical == "н":
		y = x / 2
		print(round(y))
	else:
		print(logical + " : недопустимое значение!")
		do(y)

main()