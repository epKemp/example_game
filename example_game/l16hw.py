import pygame
import time
import random

WIDTH = 700  # ширина окна
HEIGHT = 540  # высота окна

pygame.init()  # инициализация(запуск) pygame
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # размер окна(экрана)

image = pygame.image.load('pic/fish.png')
"""загрузка главного изображения"""
hero = pygame.image.load('pic/hero.png')
x = 400
y = 320
hero1 = pygame.image.load('pic/hero1.png')
"""загрузка окружения"""
meteor = pygame.image.load('pic/meteor.png')
space = pygame.image.load('pic/space.png')
x_space = 0
y_space = 0
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
show_text = True
"""текст"""
font_100 = pygame.font.Font("fonts/base.ttf", 100) # None - файл с шрифтом. ttf, 100 - размер шрифта
font_75 = pygame.font.Font(None, 75)
font_20 = pygame.font.Font(None, 20)
text = font_100.render("название игры", True, [255, 255, 255])
text_score = font_75.render("Счет:", True, [255, 255, 255])
info_u = font_20.render("w - вверх", False, [255, 255, 255])
info_l = font_20.render("a - влево", True, [255, 255, 255])
info_r = font_20.render("d - вправо", True, [255, 255, 255])
info_d = font_20.render("s - вниз", True, [255, 255, 255])
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
            show_text = False
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
            if event.key == pygame.K_LSHIFT:
                speed += 1
            if event.key == pygame.KMOD_CTRL:
                speed -= 1
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
            if event.key == pygame.K_LSHIFT:
                speed -= 1
            if event.key == pygame.KMOD_CTRL:
                speed += 1
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

    if x <= -1:
        #x = 700 - 100
        x += speed
        bg_color = blue

    if x >= 612:
        #x = 0
        x -= speed
        bg_color = black

    if y >= 445:
        #y = 1
        y -= speed
        bg_color = d_blue

    if y <= -1:
        #y = 540 - 100
        y += speed
        bg_color = dd_blue
    "движение кометы"
    if x_comet >= 0:
        x_comet += 1
    if x_comet >= 700 - 50:
        x_comet = 0
    #if x_comet1 <=750:
        x_comet1 -= 1
    #wif x_comet1 <=0:
        #x_comet = 750
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
    #screen.blit(space,(x_space, y_space))
    if show_text:
        screen.blit(text, (0, 0))
        screen.blit(text_score, (0, 100))
        screen.blit(info_u, (638, 0))
        screen.blit(info_l, (638, 20))
        screen.blit(info_d, (638, 40))
        screen.blit(info_r, (638, 60))
    screen.blit(hero, (x, y))
    screen.blit(comet, (x_comet, y_comet))

    #for i in range(2):
       # screen.blit(fire, (241, 342))
        #screen.blit(meteor, (365, 273))
    if bg_color == d_blue:
        print('1 level')
    elif bg_color == dd_blue:
        print('2 level')
        screen.blit(meteor, (375, 363))
    elif bg_color == black:
        print('3 level')
        screen.blit(meteor, (10, 0))
    elif bg_color == blue:
        print('4 level')
        screen.blit(meteor, (540, 0))
        #screen.blit(comet1, (x_comet1, y_comet1))
    # обновление
    pygame.display.flip()
# завершение работы программы (удаление временных файлов)
pygame.quit()