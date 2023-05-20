import pygame
import time
import random

WIDTH = 800  # ширина окна
HEIGHT = 640  # высота окна

pygame.init()  # инициализация(запуск) pygame
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # размер окна(экрана)

image = pygame.image.load('pic/fish.png')
"""загрузка главного изображения"""
hero = pygame.image.load('pic/hero.png')
x = 400
y = 320
"""загрузка окружения"""
meteor = pygame.image.load('pic/meteor.png')
comet = pygame.image.load('pic/comet.png')
x_comet = 0
y_comet = 50
comet1 = pygame.image.load('pic/comet1.png')
x_comet1 = 750
y_comet1 = 590
fire = pygame.image.load('pic/fire.png')
speed = 1
go_up = False
go_down = False
go_right = False
go_left = False
changecolor = False
"""формат rgb(red green blue)"""
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
g_yel = (240, 214, 152)
d_blue = (6, 23, 76)
dd_blue = (2, 14, 49)
bg_color = d_blue
colors = [d_blue, dd_blue,black, blue]

"""игровой цикл"""
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #elif event.type == pygame.MOUSEMOTION:
            #print('движение мыши')
        #elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
            #print('клик')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                go_up = True
                y -= speed
            if event.key == pygame.K_s:
                go_down = True
                y += speed
            if event.key == pygame.K_d:
                go_right = True
                x += speed
            if event.key == pygame.K_a:
                go_left = True
                x -= speed
        #if event.key == pygame.K_SPACE:
            #random.choice(colors)
            #pygame.display.flip()


            # elif event.type == pygame.K_LEFT:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                go_up = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_s:
                go_down = False
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_a:
                go_left = False


        # print(event)

    # движение
    if go_up == True:
        y = y - speed
    if go_down == True:
        y = y + speed
    if go_right == True:
        x += speed
    if go_left == True:
        x -= speed
    if changecolor == True:
        random.choice(colors)

    if x == 0:
        x = 800 - 100
        bg_color = blue

    if x == 800:
        x = 0
        bg_color = black

    if y == 640:
        y = 1
        bg_color = d_blue

    if y == 0:
        y = 640 - 100
        bg_color = dd_blue
    "движение кометы"
    if x_comet >= 0:
        x_comet += 1
    if x_comet >= 800 - 50:
        x_comet = 0
    #if x_comet1 <=750:
        x_comet1 -= 1
    #wif x_comet1 <=0:
        x_comet = 750
    # x -= speed
    # y -= speed
    # if y <= 0:
    # y += speed
    # if x <= 0 :
    # x += speed
    # print('x', x)
    # print('y', y)

    # отрсивока
    screen.fill(bg_color)
    screen.blit(hero, (x, y))
    for i in range(2):
        screen.blit(fire())
    if bg_color == d_blue:
        print('1 level')
    elif bg_color == dd_blue:
        print('2 level')
        screen.blit(meteor, (375, 363))
    elif bg_color == black:
        print('3 level')
        screen.blit(meteor, (10, 0))
        screen.blit(comet, (x_comet, y_comet))
    elif bg_color == blue:
        print('4 level')
        screen.blit(meteor, (640, 0))
        #screen.blit(comet1, (x_comet1, y_comet1))
    # обновление
    pygame.display.flip()
# завершение работы программы (удаление временных файлов)
pygame.quit()