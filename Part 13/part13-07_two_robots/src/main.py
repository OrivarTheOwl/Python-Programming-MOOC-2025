# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x1 = 0
x2 = 0

y1 = 50
y2 = 150

speed_1 = 1
speed_2 = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x1, y1))
    window.blit(robot, (x2, y2))
    pygame.display.flip()
    
    x1 += speed_1
    x2 += speed_2

    if x1 == 0 or x1+robot.get_width() == 640:
        speed_1 = -speed_1

    if x2 == 0 or x2+robot.get_width() == 640:
        speed_2 = -speed_2


    clock.tick(60)