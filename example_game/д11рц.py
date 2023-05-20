import pygame
import time

WIDTH = 800#ширина окна
HEIGHT = 640#высота окна

pygame.init()#инициализация(запуск) pygame
screen = pygame.display.set_mode([WIDTH, HEIGHT])# размер окна(экрана)

#формат rgb(red green blue)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
g_yel = (240,214,152)
a = 0
#игровой цикл
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        print(event)
        print(event(1024))
    # отрсивока
    #while a != 1:
        screen.fill(g_yel)
        #pygame.display.flip()
        #time.sleep(3)
        #screen.fill(black)
        #pygame.display.flip()
        #time.sleep(3)
        #screen.fill(white)
        #pygame.display.flip()
        #time.sleep(3)
    # обновление
pygame.display.flip()
#завершение работы программы (удаление временных файлов)
pygame.quit()