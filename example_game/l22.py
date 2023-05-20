from random import choice
spisok = ['a', 'b', 'c']
spisok_2 = ['1', '2', '3']
pole = choice(spisok) + choice(spisok_2)
korabl = ['a1', 'b2', 'c3']
kolichestvo = 3
print('Игра в морсой бой!')
print('Компьютер расставил 3 однопалубных корабля на поле 3 на 3')
print('Попробуйте их уничтожить')
while korabl != []:
    a = input('введите поле: ')
    for i in korabl:
        if a == i:
            print('вы попали в корабль: ')
            korabl.remove(i)
            kolichestvo -= 1
            break
        else:
            print('промах')
            break
        print(kolichestvo)
print('Спасибо за игру!')