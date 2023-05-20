import pygame
import time
import random


WIDTH = 700  # ширина окна
HEIGHT = 540  # высота окна

pygame.init()  # инициализация(запуск) pygame
screen = pygame.display.set_mode([WIDTH, HEIGHT])  # размер окна(экрана)
pygame.display.set_caption('example game')

image = pygame.image.load('pic/fish.png')
"""загрузка главного изображения"""
hero = pygame.image.load('pic/hero.png')
x = 400
y = 320
hero1 = pygame.image.load('pic/hero1.png')
hero_rect = hero.get_rect()
hero_rect.center = x, y
hero1_rect = hero1.get_rect()
hero1_rect.center = x, y
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
show_info_text = False

"""текст"""
font_100 = pygame.font.Font("fonts/base.ttf", 100) # None - файл с шрифтом. ttf, 100 - размер шрифта
font_75 = pygame.font.Font(None, 75)
font_40 = pygame.font.Font("fonts/base.ttf", 40)
font_20 = pygame.font.Font("fonts/count.ttf", 20)
font_25 = pygame.font.Font("fonts/base.ttf", 25)
text = font_100.render("название игры", True, [255, 255, 255])
text_rect = text.get_rect()
text_rect.center = WIDTH // 2, 40
text_score = font_20.render("Счет: 0", True, [255, 255, 255])
#dict_4 = {}

text_begin = font_40.render('Начать', True, [255,255,255])
text_begin_active = font_40.render('Begin', True, [0,0,0])
text_begin_rect= text_begin.get_rect()
text_begin_rect.center = WIDTH // 2, HEIGHT // 2
text_continue = font_40.render('Продолжить', True, [255,255,255])

text_info = font_40.render('Информация', True, [255, 255, 255])
text_info_active = font_40.render('Info', True, [0, 0, 0])
text_info_rect = text_info.get_rect()
text_info_rect.center = WIDTH // 2, HEIGHT //2 + 50

text_end = font_40.render('выйти', True, [255,255,255])
text_end_active = font_40.render('exit', True, [0,0,0])
text_end_rect = text_end.get_rect()
text_end_rect.center = WIDTH // 2, HEIGHT // 2 + 100

info_u = font_20.render("w - вверх", False, [255, 255, 255])
info_l = font_20.render("a - влево", True, [255, 255, 255])
info_r = font_20.render("d - вправо", True, [255, 255, 255])
info_d = font_20.render("s - вниз", True, [255, 255, 255])
info_u_rect = info_u.get_rect()
info_l_rect = info_l.get_rect()
info_r_rect = info_r.get_rect()
info_d_rect = info_d.get_rect()
info_u_rect.center = WIDTH -70, HEIGHT - 70
info_l_rect.center = WIDTH -70, HEIGHT - 50
info_r_rect.center = WIDTH -80, HEIGHT - 10
info_d_rect.center = WIDTH -57, HEIGHT - 30
"""формат rgb(red green blue)"""
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
g_yel = (240, 214, 152)
d_blue = (6, 23, 76)
dd_blue = (2, 14, 49)
bg_color = (120,219,226)
colors = [d_blue, dd_blue,black, blue]

"""игровой цикл"""
run = True
while run:
    mouse_pos = pygame.mouse.get_pos()
    mouse_keys = pygame.mouse.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #elif event.type == pygame.MOUSEMOTION:
            #print('движение мыши')
        #elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.MOUSEBUTTONDOWN:
            #print('клик')
        if event.type == pygame.KEYDOWN:
            #show_text = False
            #text = font_25.render("название игры", True, [255, 255, 255])
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
    """нажатие мыши"""
    # if event.type == pygame.MOUSEBUTTONDOWN:
    #     if event.button == 1:
    #         print('LKM')
    #     if event.button == 2:
    #         print('kolesiko')
    #     if event.button == 3:
    #         print('pkm')
    # """отпускаине мыши"""
    # if event.type == pygame.MOUSEBUTTONUP:
    #     if event.button == 1:
    #         print('')
    #     if event.button == 2:
    #         print('kolesiko')
    #     if event.button == 3:
    #         print('pkm')
    # if mouse_keys[0]:
    #     print('lkm')
    # if mouse_keys[1]:
    #     print('kolesiko')
    # if mouse_keys[2]:
    #     print('pkm')
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

    if mouse_keys[2]:
        show_text = True
        bg_color == (120, 219, 226)

    if show_text:

        if text_begin_rect.collidepoint(mouse_pos):
            screen.blit(text_begin_active, text_begin_rect)
            if mouse_keys[0]:
                show_text = False
                bg_color = d_blue
        else:
            screen.blit(text_begin, text_begin_rect)

        if text_end_rect.collidepoint(mouse_pos):
            if mouse_keys[0]:
                run = False
            screen.blit(text_end_active, text_end_rect)
        else:
            screen.blit(text_end, text_end_rect)
        screen.blit(text, text_rect)

        if text_info_rect.collidepoint(mouse_pos):
            if mouse_keys[0]:
                screen.blit(text_info_active, text_info_rect)
                show_info_text = True
            screen.blit(text_info, text_info_rect)
        else:
            screen.blit(text_info, text_info_rect)
        screen.blit(text_info,text_info_rect)

    if show_info_text:
        screen.blit(info_u, info_u_rect)
        screen.blit(info_r, info_r_rect)
        screen.blit(info_d, info_d_rect)
        screen.blit(info_l, info_l_rect)
    if show_text == False:
        show_info_text = False
        #screen.blit(info_u, (638, 0))
        #screen.blit(info_l, (638, 20))
        #screen.blit(info_d, (638, 40))
        #screen.blit(info_r, (638, 60))
    #screen.blit(text_score, (0, 100))
    #for i in range(1, 101):
         #dict_4.update({f'{i}': i})
    screen.blit(hero, (x, y))
    # if hero_rect.collidepoint(mouse_pos):
    #     if mouse_keys[0]:
    #         screen.blit(hero1, (x, y))
    # else:
    #     screen.blit(hero, (x, y))

    screen.blit(comet, (x_comet, y_comet))

    #for i in range(2):
       # screen.blit(fire, (241, 342))
    if bg_color == (120,219,226):
        None
    elif bg_color == d_blue:
        print('level 1')
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