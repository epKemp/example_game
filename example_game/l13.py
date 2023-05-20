import pygame
import time

WIDTH = 800#ширина окна
HEIGHT = 640#высота окна

pygame.init()#инициализация(запуск) pygame
screen = pygame.display.set_mode([WIDTH, HEIGHT])# размер окна(экрана)

image = pygame.image.load('pic/fish.png')
x = 400
y = 320
speed = 1 
go_up = False
go_down = False
go_right = False
go_left = False
#формат rgb(red green blue)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
g_yel = (240, 214, 152)
bg_color = g_yel

#игровой цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEMOTION:
            print('движение мыши')
        elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
            print('клик')
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                go_up = True
                y -= speed
            if event.key == pygame.K_DOWN:
                go_down = True
                y += speed
            if event.key == pygame.K_RIGHT:
                go_right = True
                x += speed
            if event.key == pygame.K_LEFT:
                go_left = True
                x -= speed




            #elif event.type == pygame.K_LEFT:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                go_up = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                go_down = False
            if event.key == pygame.K_RIGHT :
                go_right = False
            if event.key == pygame.K_LEFT:
                go_left = False
        #print(event)
    #движение
    if go_up == True:
        y = y - speed
    if go_down == True:
        y = y + speed
    if go_right == True:
        x += speed
    if go_left == True:
        x -= speed

    if x == 0 :
        x = 800 - 50
        bg_color = (0, 0 ,0 )

    if x == 800:
        x = 0
        bg_color = (127,255,212)

    if y == 640:
        y = 1
        bg_color = (237,60,202)

    if y == 0:
        y = 640 - 50
        bg_color = (205,149,117)


    #x -= speed
    #y -= speed
    #if y <= 0:
        #y += speed
    #if x <= 0 :
        #x += speed
    #print('x', x)
    #print('y', y)
    # отрсивока
    screen.fill(bg_color)
    screen.blit(image, (x, y))
    # обновление
    pygame.display.flip()
#завершение работы программы (удаление временных файлов)
pygame.quit()