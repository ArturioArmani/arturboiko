﻿import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)


far = int(input("Сколько градусов "))
print("В фаренгейтах " + str((far-32)/1.8))
print("В кельвин " + str(far + 273.15))

