def add(a, b):
    s= a + b
    print( 'сумма =', s)

add(1, 2)
def add_all(*args):
    s = 0
    for i in args:
        s += i
    print(args)
    print(s)
add_all(1,45,6,87,9)


def kvadr(*args):
   # s =[]
    for i in args:
        i = i**2
        print(i)

kvadr(1, 4, 6)

def count_fib(c):
    a = 0
    b = 1
    for i in range(c):
        k1 = a +b
        a = b
        b = k1
        print(k1, end = ' ')
    print()

count_fib(100)

def add_2(a= 0, b=0):
    return a + b
c = add_2(3,4)
print(c)


def raz(a = 0, b=0):
    if a < b:
        s = a
        a = b
        b = s
    return a - b
c = raz(4,3)
print(c)

def delit(a=0,b=0):
    if a < b:
        a =b
        b=a
    return a // b
c = delit(3,6)
print(c)


def umn(a = 1, b =1):
    return a * b
c = umn(3,4)
print(c)


def add_3(a , b):
    s = 0
    for i in range(a,b):
        s = s + i
print(i,s)



may_2020 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22, 11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
may_2021 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25, 21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]

def comfort_count(temperatures):
    may_2020 = [24, 26, 15, 10, 15, 19, 10, 1, 4, 7, 7, 7, 12, 14, 17, 8, 9, 19, 21, 22,
                11, 15, 19, 23, 15, 21, 16, 13, 25, 17, 19]
    may_2021 = [20, 27, 23, 18, 24, 16, 20, 24, 18, 15, 19, 25, 24, 26, 19, 24, 25,
                21, 17, 11, 20, 21, 22, 23, 18, 20, 23, 18, 22, 23, 11]
