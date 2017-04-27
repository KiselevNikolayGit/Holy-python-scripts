import pickle

def write(Notes):
    Notebook = open('note', 'wb')
    pickle.dump(Notes, Notebook)
    Notebook.close()

def read():
    Notebook = open('note', 'rb')
    Notes = pickle.load(Notebook)
    Notebook.close()
    return Notes

def show(Notes):
    Index = 1
    for note in Notes.items():
        print('______________________________(%i)' % Index)
        print('-' + str(note[0]).upper() + '-')
        print(note[1])
        Index += 1
    print('\n')

def add(Notes):
    Tit = input('Title: ')
    Bod = input(' Body: ')
    Notes.update({Tit: Bod})
    return Notes

try:
    read()
except IOError:
    write(dict(Hello='This is your 1st note!'))

Work = True
while Work:
    Notes = read()
    show(Notes)
    An = input('type Enter for new note\nor "c" for clear\nor number of note, if you want to del note\nor "n" for stop >> ')
    #Посмотрим не указал ли пользователь число
    try:
        Notes.pop(list(Notes.keys())[int(An) - 1])
        write(Notes)
        print('\n\nWe Del note No%s.' % An)
    except ValueError:
        if An == '':
            print('\n\n\tNew note')
            Notes = add(Notes)
            write(Notes)
        elif An == 'c' or An == 'с': #Учитываем оба языка, спасая от боли
            write({})
        else:
            Work = False
