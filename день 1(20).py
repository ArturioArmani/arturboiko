import datetime
def printTimeStamp(name):
 print('Автор програми: ' + name)
 print('Час компіляції: ' + str(datetime.datetime.now()))
name = 'Бойко Артур'
printTimeStamp(name)


bread = int(input("Scolco vcherashnego hleba ti hochesh? "))
new_bread = bread * 8.5
print("Esli bi ti kupil svezii hleb ti bi zaplatil %.2f $" % new_bread)
scidca = new_bread * 0.60
print("Tvoia scidka = %.2f $" % scidca)
real_bread = new_bread - scidca
print("Zaplati  %.2f $" % real_bread)

