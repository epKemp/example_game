"""
dict_1.clear() #очищает словарь
dict_1.copy() #возвращает копию словаря
dict_1.get #возвращает значеник ключа, если нет, возвращает None
dict_1.items #возвращает пары(ключ, значение)
dict_1.pop #
dict_1.popitem#

"""
list_1 = [] #список
str_1 = '' #строка
tuple_1 = () #кортеж


slovar_1 = {'Федор' : 13, 'Петр' : 14, 'Вероника' : 12} #словарь
slovar_2 = {'a' : 100, 'b' : 150, 'c' : 200, 'd': 400}
dict_3 = {}
keys = ['red', 'black', 'white']
values = [(255, 0, 0), (0,0,0), (255, 255, 255)]
#dict_1.clear()    # очищает словарь
#print(dict_1)
# dict_2 = dict_1.copy()  # возвращает копию словаря
# print(dict_2)
#dict_2.update(dict_1)  # обновляет словарь значениеми из dict_1
#print(dict_2)
#a = dict_2.get('abc')  # возвращает значение по ключу, если нет, возвращает None
#print(a)
#a, b, c = dict_1.items()  # возвращает пары (ключ, значение)
#print(a, b, c)
#dict_1.pop('Петр')  # удаляет пару (ключ, значение) по ключу.
#print(dict_1)
a, b, c = dict_1.values()  # возвращает значения в словаре
print(a, b, c)
# 1
"""
dict_3.update(dict_1)
dict_3.update(dict_2)
print(dict_3)"""
# 2


"очистка словаря"
#slovar_1.clear()

"копирование словаря"
#dict_3 = slovar_1.copy()



