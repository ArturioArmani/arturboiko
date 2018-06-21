import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)



def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

print(fac(5))

