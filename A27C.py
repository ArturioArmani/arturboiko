import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)




import random
t = open("password.txt", 'r')
text = t.readlines()

password = text[random.randint(0, len(text) - 1)].title() + text[random.randint(0, len(text) - 1)]
print(password)
t.close()


