import pygame
import time

WIDTH = 700#ширина окна
HEIGHT = 540#высота окна

pygame.init()#инициализация(запуск) pygame
screen = pygame.display.set_mode([WIDTH, HEIGHT])# размер окна(экрана)

#image = pygame.image.load('pic/slime.png')
image1 = pygame.image.load('pic/fish.png')
x = 325
y = 255
speed = 1
#формат rgb(red green blue)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
g_yel = (240,214,152)

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
        #print(event)
    """x += speed
    y += speed
    if y >= 490:
        y -= speed
    if x >= 650 :
        x -= speed"""
    """x -= speed
    y += speed
    if x <= 0:
        x += speed
    if y >= 490:
        y -= speed"""
    """x -= speed
    y -= speed
    if x <= 0:
        x += speed
    if y <= 0:
        y += speed"""
    """x += speed
    y -= speed
    if x >= 650:
        x -= speed
    if y <= 0:
        y += speed"""
    """x += speed
    if x >= 400:
        screen.fill(red)
        pygame.display.flip()
    if x >= 650:
        x -= speed"""
    print('x', x)
    print('y', y)
    # отрсивока
    #if x <= 400:
       #screen.fill(g_yel)
    screen.fill(g_yel)
    #screen.blit(image, (0, 0))
    screen.blit(image1, (x, y))

    # обновление
    pygame.display.flip()
#завершение работы программы (удаление временных файлов)
pygame.quit()