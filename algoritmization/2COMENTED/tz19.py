# Задание
# Напишите программу по следующему условию:
# У пользователя запрашивается ввод трех нецелых чисел, после чего записывает квадрат наибольшего из них в файл output.txt в формате: «The greatest value square is ЧИСЛО» 

import math

FLOAT1 = float(input("Нецелое число: "))
FLOAT2 = float(input("Нецелое число: "))
FLOAT3 = float(input("Нецелое число: "))

POW1 = math.pow(FLOAT1) # Нахождение квадрата чисел
POW2 = math.pow(FLOAT2) # Нахождение квадрата чисел
POW3 = math.pow(FLOAT3) # Нахождение квадрата чисел

RESULT = max(POW1, POW2, POW3) # максиамальное

FILE = open('output.txt', 'w') # Создание файла для вывода output.txt

FILE.write("The greatest value square is " + str(RESULT)) # Запись в файл
FILE.close() # Окончание работы с файлом