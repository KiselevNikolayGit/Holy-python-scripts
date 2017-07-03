run = True
while run:
    try:
        poems_file = open('poems.txt', 'r', encoding = 'UTF-8')
        poems = poems_file.read()
    except FileNotFoundError:
        poems_file = open('poems.txt', 'w', encoding = 'UTF-8')
        poems = ''
    poems_file.close()

    print(poems)

    for r in range(3):
        print('\n')

    cashe = open('ca.she', 'w', encoding = 'UTF-8')
    cashe.close()
    text_line = ''
    number_line = -1

    while text_line != '---\n' and text_line != '#clear\n'and text_line != '#save\n' :
        number_line += 1
        lable = str(number_line) + ' '
        while len(lable) <= 5:
            lable = '-' + lable
        text_line = input(lable)
        if text_line != '#back':
            text_line += '\n'
            if number_line == 0:
                text_line = text_line.upper()
            else:
                text_line = text_line.capitalize()
            cashe = open('ca.she', 'a', encoding = 'UTF-8')
            cashe.write(text_line)
            cashe.close()
        else:
            number_line -= 2
            cashe = open('ca.she', 'r', encoding = 'UTF-8')
            dc = cashe.read()
            cashe.close()
            dcedited = dc.split('\n')
            dcedited.pop()
            delited = dcedited.pop()
            cashe = open('ca.she', 'w', encoding = 'UTF-8')
            normadc = ''
            for d in dcedited:
                normadc += d + '\n'
            cashe.write(normadc)
            cashe.close()
            print('DELETED: ' + str(delited))


    if text_line == '#clear\n':
        poems_file = open('poems.txt', 'w', encoding = 'UTF-8')
        poems_file.write('')
        poems_file.close()
    elif text_line == '#save\n':
        run = False
    else:
        poems_file = open('poems.txt', 'w', encoding = 'UTF-8')
        cashe = open('ca.she', 'r', encoding = 'UTF-8')
        new = cashe.read()
        new = new.split('%')
        for procanted in range(len(new)) :
            new[procanted] = new[procanted].capitalize()
        new = ''.join(new)
        cashe.close()
        poems_file.write(poems + '---\n' + new)
        poems_file.close()

    for r in range(3):
        print('\n')
