# Задание
# Напишите программу по следующему условию:
# Известно, что в файле input.txt содержатся 3 строки, на каждой из которых записано целое число. Напишите программу для считывания трех этих чисел в список и вывод на экран их суммы. 

FILE = open('input.txt', 'r') # Создание файла для вывода output.txt

TEXT_FILE = FILE.read() # Считать файл
FILE.close() # Окончание работы с файлом

LIST_FILE = TEXT_FILE.split("\n")

LIST = []
SUM = 0

for NUMBER in LIST_FILE:
	SUM += int(NUMBER)
	LIST.append(int(NUMBER))

print(LIST)
print("Сумма = " + str(SUM))
