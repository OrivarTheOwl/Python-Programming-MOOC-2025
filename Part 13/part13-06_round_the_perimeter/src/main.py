# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

x = 0
y = 0

horizontal = 1
vertical = 0

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(robot, (x, y))
    pygame.display.flip()
    
    if horizontal > 0 and x+robot.get_width() >= 640:
        horizontal = 0
        vertical = 1
    elif horizontal < 0 and x <= 0:
        horizontal = 0
        vertical = -1
    elif vertical > 0  and y+robot.get_height() >= 480:
        horizontal = -1
        vertical = 0
    elif vertical < 0 and y <= 0:
        horizontal = 1
        vertical = 0

    x += horizontal
    y += vertical

    clock.tick(60)