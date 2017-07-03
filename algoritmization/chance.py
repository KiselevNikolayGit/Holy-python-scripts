raw = input('Ваши оценки через запятую: ').split(',')
a = []
for letter in raw:
	a.append(int(letter))
s = 0
supers = 0
norm_mark = int(input('Оценка, которая вас устроит: '))
for mark in a:
	s += mark
	if mark >= norm_mark:
		supers += 100 / len(a)
b = s / len(a)
print('Средний бал: %f' % b) # Cредний бал
print('Вы сдадите ' + str(supers) + '%')
