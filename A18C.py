﻿import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)





def rec(x):
    if x == 1:
        return 1
    else:
        return (1 / x) + rec(x - 1)

print(rec(5))


