# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()

width = 640
height = 480
window = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")

x = width/2-ball.get_width()/2
y = height/2-ball.get_height()/2

x_bound = width-ball.get_width()
y_bound = height-ball.get_height()

horizontal = 2
vertical = 2

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    window.fill((0, 0, 0))
    window.blit(ball, (x, y))
    pygame.display.flip()
    
    if x <= 0 or x >= x_bound:
        horizontal = -horizontal

    if y <= 0 or y >= y_bound:
        vertical = -vertical

    x += horizontal
    y += vertical

    clock.tick(60)