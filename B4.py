﻿import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)



hv = int(input("Hvilin "))
sms = int(input("SMS "))

summ = 15
summ2 = 0

if hv > 200:
    summ += hv - 200 * 0.17
if sms > 50:
    summ += sms - 50 * 0.15

summ2 = summ + summ * 0.05 + 0.44

print("Без комисии ти заплатиш %.2f $" % summ)
print("Ти заплатиш %.2f $" % summ2)


