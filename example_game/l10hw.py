"""import random
import time
width = 50
print('Название игры')
left_len = 20
gap_len = 10
#end = random.randint(50, 200)
# n = 0
while True:
    # if n == end:
    # break
    # else:
    # pass
    right_len = width - gap_len - left_len
    rand = random.randint(0, 3)
    print(('#' * left_len) + (' ' * gap_len) + ('#' * right_len))
    if left_len > 1 and rand == 1:
        left_len = left_len - 1
    elif left_len + gap_len < width - 1 and rand == 2:
        left_len = left_len + 1
    # n = n + 1
    time.sleep(0.1)
print(('#' * left_len) + ('_' * gap_len) + ('#' * right_len))
print('Конец игры')
print(len.gap_len)
""""""
import time
t  = int(input('введите время в секундах'))
a = 0
while a!= 'стоп':
    t = t - 1
    time.sleep(1)

    print(t)
    if t == 0:

        break
"""
import random
import time
width = 50
print('Название игры')
left_len = 20
gap_len = 10
#end = random.randint(50, 200)
# n = 0
while True:
# if n == end:
# break
# else:
# pass
    right_len = width - gap_len - left_len
    rand = random.randint(0, 3)
    print(('#' * left_len) + (' ' * gap_len) + ('#' * right_len))
    if left_len > 1 and rand == 1:
        left_len = left_len - 1
    elif left_len + gap_len < width - 1 and rand == 2:
        left_len = left_len + 1
# n = n + 1
time.sleep(0.1)
print(('#' * left_len) + ('_' * gap_len) + ('#' * right_len))
print('Конец игры')

