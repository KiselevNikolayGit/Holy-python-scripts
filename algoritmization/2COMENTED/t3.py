# Задание
# Напишите программу по заданному условию:
# Программа должна вывести на экран сумму двух произвольных чисел в диапазоне от 10 до 15 

NUM_A = int(input('a = ')) # Запрос на первое число
NUM_B = int(input('b = ')) # Запрос на второе число

SUM = NUM_A + NUM_B # Нахождение суммы

if SUM > 10 and SUM < 15: # Проверка вхождения суммы в диапозон
	print(SUM) # Вывод суммы если сумма нормальное число
else: # Иначе
	print("Сумма вне зоны") # Вывод ошибки