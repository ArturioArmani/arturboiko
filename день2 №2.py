﻿import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)


a=list(map(int,input("aa:").split(" ")))
if int(0) in a:
    a.remove(0)
    a.sort()
    print(a)
else:
    print("Некоректне введення")
