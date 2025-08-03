# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")


robot_width = robot.get_width()
robot_height = robot.get_height()

x_pos = 50
y_pos = 100

screen.fill((0, 0, 0))

for i in range(10):
    for j in range(10):
        screen.blit(robot, (x_pos/2, y_pos))
        x_pos += robot_width*1.5
    x_pos = 50 + 25*(i+1)
    y_pos += 20


pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()