# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_count = 1000

x_bound = width-robot.get_width()
y_bound = height-robot.get_height()

screen.fill((0, 0, 0))

for i in range(robot_count):
    screen.blit(robot, (randint(0, x_bound), randint(0, y_bound)))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()