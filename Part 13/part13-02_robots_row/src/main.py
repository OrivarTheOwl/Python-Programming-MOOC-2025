# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
robot_count = 10

robot_width = robot.get_width()
robot_height = robot.get_height()

x_pos = (width-(robot_width * robot_count))/2
y_pos = 240-robot_height/2

screen.fill((0, 0, 0))

for i in range(robot_count):
    screen.blit(robot, (x_pos, y_pos))
    x_pos += robot_width


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()