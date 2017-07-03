from datetime import datetime
print ('''████──█──█──█──█──████──███
█──█──█─█───██─█──█──█───█
█─────██────█─██──█──█───█
█──█──█─█───█──█──█──█───█
████──█──█──█──█──████───█''')
print ('cknot-text')
print ('type ">vr" to overwrite')
c = open ('data.txt', 'r')
print (c.read())
c.close ()

while True: 
    string = input ('add:')
    if not string == '>vr':
        kite = open ('data.txt', 'a')
        timenow = datetime.now()
        kite.write ( '<<<' + str (timenow) + '>>>\n' + string + '\n')
    else: kite = open ('data.txt', 'w')
    kite.close ()
    c = open ('data.txt', 'r')
    print (c.read())
    c.close ()
