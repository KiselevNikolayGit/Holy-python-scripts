# -*- coding: utf-8 -*-
import pickle

#Some kind of logo:)
print('''  _____                 _   _       _       \n / ____|               | \ | |     | |      \n| (___   __ ___   _____|  \| | ___ | |_ ___ \n \___ \ / _` \ \ / / _ \ . ` |/ _ \| __/ _ \ \n ____) | (_| |\ V /  __/ |\  | (_) | ||  __/\n|_____/ \__,_| \_/ \___|_| \_|\___/ \__\___|\n''')

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
    An = input('type Enter for new note\nor number of note, if you want to del note\nor "c" for clear\nor "n" for stop >> ')
    try:
        Notes.pop(list(Notes.keys())[int(An) - 1])
        write(Notes)
        print('\n\nWe Del note No%s.' % An)
    except ValueError:
        if An == '':
            print('\n\n\tNew note')
            Notes = add(Notes)
            write(Notes)
        elif An == 'c' or An == 'с':
            write({})
        else:
            Work = False
