import random
import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)


def password():
    passw = ''
    for i in range(random.randint(8,17)):
        passw += chr(random.randint(33, 127))
    print(passw.encode("ascii"))

for i in range(10):
    password()



