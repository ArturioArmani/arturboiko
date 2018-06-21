import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)



def taxi(metr, price):
   summ = 25 + price * (metr//140)
   return summ

print(taxi(1200, 2))


