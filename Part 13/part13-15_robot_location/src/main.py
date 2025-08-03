# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
width = 640
height = 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")

left_bound = 0
right_bound = width-robot.get_width()
upper_bound = 0
lower_bound = height-robot.get_height()

robot_x = 0
robot_y = 0
mouse_x = 0
mouse_y = 0

clock = pygame.time.Clock()

while True:
    robot_right = robot_x + robot.get_width()
    robot_bottom = robot_y + robot.get_height()

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]

        if mouse_x >= robot_x and mouse_x <= robot_right and mouse_y >= robot_y and mouse_y <= robot_bottom:
            robot_x = randint(left_bound, right_bound)
            robot_y = randint(upper_bound, lower_bound)

        if event.type == pygame.QUIT:
            exit(0)

    window.fill((0, 0, 0))
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()

    clock.tick(60)