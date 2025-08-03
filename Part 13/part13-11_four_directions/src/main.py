# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

width = 640
height = 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

x = width/2-robot.get_width()/2
y = height/2-robot.get_height()/2

left = False
right = False
up = False
down = False

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False

        if event.type == pygame.QUIT:
            exit()

    if left:
        x -= 2
    if right:
        x += 2
    if up:
        y -= 2
    if down:
        y += 2

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()

    clock.tick(60)