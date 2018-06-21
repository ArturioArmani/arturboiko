import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)

r = int(input('Введите радиус - '))

s = math.pi * r ** 2  # Площа круга

v = 3 / 4 * math.pi * r ** 3  # Объем кулі

print("Площадь круга = {}, Объем шара = {}".format(s, v))
