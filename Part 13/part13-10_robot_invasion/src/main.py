# WRITE YOUR SOLUTION HERE:

import pygame
from random import randint, choice

pygame.init()

width = 640
height = 480
window = pygame.display.set_mode((width, height))

robot_img = pygame.image.load("robot.png")
robot_count = 20

x_bound = width-robot_img.get_width()
y_bound = height-robot_img.get_height()

robot_list = []

for i in range(robot_count):
    robot_data = {
        "x": randint(0, x_bound),
        "y": randint(0-y_bound*2, 0-robot_img.get_height()),
        "horizontal": 0,
        "vertical": 1,
        "has_landed": False
        }
    robot_list.append(robot_data)

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0, 0, 0))

    for robot in robot_list:
        if robot["y"] >= y_bound and robot["has_landed"] == False:
            robot["horizontal"] = choice([-1, 1])
            robot["vertical"] = 0
            robot["has_landed"] = True

        robot["x"] += robot["horizontal"]
        robot["y"] += robot["vertical"]
        window.blit(robot_img, (robot["x"], robot["y"]))
    
    pygame.display.flip()
    

    clock.tick(240)