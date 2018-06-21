import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)





t = open('minecraft.txt', 'r')
for i in range(10):
    print(t.readline())

t.close()


