import pickle

print('Укажите ваши\n')
toxic_dump = dict(
    firstname=(input('Имя: ')),
    lastname=(input('Фамилию: ')),
    age=(input('Возраст: ')),
    properties=(input('Рост, Вес, Размер обуви (через запятую): ')))

river = open('user', 'wb')
pickle.dump(toxic_dump, river)
river.close()

print('Проверьте:', end=' ')
test = open('user', 'rb')
print(pickle.load(test))
test.close()
