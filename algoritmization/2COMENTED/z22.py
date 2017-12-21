# Задание
# Напишите программу по следующему условию:
# Известно, что в файле input.txt содержатся 2 строки, на каждой из которых записано нецелое число. Напишите программу для считывания двух этих чисел в список и вывод на экран их остатков. 

FILE = open('input.txt', 'r') # Создание файла для вывода output.txt

TEXT_FILE = FILE.read() # Считать файл
FILE.close() # Окончание работы с файлом

LIST_FILE = TEXT_FILE.split("\n")

LIST = []
OSTATKI = []

for NUMBER in LIST_FILE:
	LIST.append(float(NUMBER))
	OSTATKI.append(float(NUMBER) % 1)

print(OSTATKI)
