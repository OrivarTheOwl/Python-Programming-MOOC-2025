# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

width = 640
height = 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

x1 = 0
y1 = 0

x2 = 100
y2 = 100

left_border = 0
right_border = width-robot.get_width()
top_border = 0
bottom_border = height-robot.get_height()

left1 = False
right1 = False
up1 = False
down1 = False

left2 = False
right2 = False
up2 = False
down2 = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left1 = True
            if event.key == pygame.K_RIGHT:
                right1 = True
            if event.key == pygame.K_UP:
                up1 = True
            if event.key == pygame.K_DOWN:
                down1 = True

            if event.key == pygame.K_a:
                left2 = True
            if event.key == pygame.K_d:
                right2 = True
            if event.key == pygame.K_w:
                up2 = True
            if event.key == pygame.K_s:
                down2 = True


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left1 = False
            if event.key == pygame.K_RIGHT:
                right1 = False
            if event.key == pygame.K_UP:
                up1 = False
            if event.key == pygame.K_DOWN:
                down1 = False

            if event.key == pygame.K_a:
                left2 = False
            if event.key == pygame.K_d:
                right2 = False
            if event.key == pygame.K_w:
                up2 = False
            if event.key == pygame.K_s:
                down2 = False


        if event.type == pygame.QUIT:
            exit()

    if left1 and x1 >= left_border:
        x1 -= 2
    if right1 and x1 <= right_border:
        x1 += 2
    if up1 and y1 >= top_border:
        y1 -= 2
    if down1 and y1 <= bottom_border:
        y1 += 2

    if left2 and x2 >= left_border:
        x2 -= 2
    if right2 and x2 <= right_border:
        x2 += 2
    if up2 and y2 >= top_border:
        y2 -= 2
    if down2 and y2 <= bottom_border:
        y2 += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()

    clock.tick(60)