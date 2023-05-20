import pygame

W = 500
H = 500

pygame.init()
screen = pygame.display.set_mode([W, H])
pygame.display.set_caption('Проверочная работа')

bee = pygame.image.load('pic/bee.png')
x = W // 2 - 25
y = H // 2 - 25
flower = pygame.image.load('pic/flower.png')
sun = pygame.image.load('pic/sun.png')

l_green = (168,228,160)

go_up = False
go_down = False
go_left = False
go_right = False
r_shift = False
go_speed = 2
text = True

f_100 = pygame.font.Font("fonts/beefont.ttf", 100)
f_80 = pygame.font.Font("fonts/beefont.ttf", 80)
begining = f_100.render('bee', True, [227,38,54])
menu = f_80.render('menu', True, [227,38,54])

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                go_up = True
                y -= go_speed
            if event.key == pygame.K_s:
                go_down = True
                y += go_speed
            if event.key == pygame.K_a:
                go_left = True
                x -= go_speed
            if event.key == pygame.K_d:
                go_right = True
                x += go_speed
            if event.key == pygame.K_RSHIFT:
                go_speed -= 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                go_up = False
            if event.key == pygame.K_s:
                go_down = False
            if event.key == pygame.K_a:
                go_left = False
            if event.key == pygame.K_d:
                go_right = False
            if event.key == pygame.K_RSHIFT:
                go_speed += 1
    if go_up == True:
        y -= go_speed
    if go_down == True:
        y += go_speed
    if go_left == True:
        x -= go_speed
    if go_right == True:
        x += go_speed

    if x <= 0 :
        x = 450
    if x >= 450:
        x = 1
    if y <= 0:
        y = 450
    if y >= 450:
        y = 1
    screen.fill(l_green)
    screen.blit(flower, (0, 0))
    screen.blit(bee, (x, y))
    screen.blit(sun, (450, 0))
    screen.blit(begining, (W//2 - 50, H//2))
    screen.blit(menu, (W//2- 70, H// 2 + 65))
    pygame.display.flip()

pygame.quit()



