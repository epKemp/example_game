import datetime
import random

"""#print('кассовый аппарат')
##price_list = []
#while price != '':
    #price_list.append(price)
   # price = input()
#print(price_list)
##print(datetime.date.today())
#for i in range(len(price_list)):
 ##print('='*25)
"""



menu = ['гамбургер = 100', 'картошка = 50', 'нагетсы = 99', 'добрая кола = 79']
menu_combo = ['гамбургер , картошка, добрая кола =250', 'гамбургер = 100', 'картошка = 50', 'нагетсы = 99', 'добрая кола = 79']
person_list = []
t = input('с собой? (yes/no)')
print(menu)
print('бери это')
print(menu_combo)
p = 10
while p != 0:
    p = int(input('что будете брать?'))
    if p == 1:
        person_list.append(menu[0])
    elif p == 2:
        person_list.append(menu[1])
    elif p == 3:
        person_list.append(menu[2])
    elif p == 4:
        person_list.append(menu[3])
    elif p == 777:
        person_list.append(menu_combo[0])
    else:
        break
    print('сейчас в корзине:', person_list)
print(datetime.date.today())
if t == 'yes':
    print('с собой')
else:
    print('на месте')
print('номер заказа:', random.randint(100, 999))
for i in range(len(person_list)):
    print('Блюдо', i + 1, person_list[i])
print('Время: ', datetime.datetime.now())