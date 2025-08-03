# WRITE YOUR SOLUTION HERE:

import pygame
import math
from datetime import datetime

pygame.init()
width = 640
height = 480
display = pygame.display.set_mode((width, height))
display.fill((0, 0, 0))

def hand_end(length: int, angle: float):
    angle -= math.pi / 2
    x = width / 2 + length * math.cos(angle)
    y = height / 2 + length * math.sin(angle)
    return (x, y)

while True:
    time = datetime.now()
    hour = time.hour
    minute = time.minute
    second = time.second

    pygame.display.set_caption(f"{hour:02d}:{minute:02d}:{second:02d}")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    display.fill((0, 0, 0))

    pygame.draw.circle(display, (255, 0, 0), (width/2, height/2), 200, 5)
    pygame.draw.circle(display, (255, 0, 0), (width/2, height/2), 10)

    second_angle = math.radians(second * 6)
    minute_angle = math.radians(minute * 6 + second * 0.1)
    hour_angle = math.radians((hour % 12) * 30 + minute * 0.5)

    pygame.draw.line(display, (0, 0, 255), (width/2, height/2), hand_end(175, second_angle), 1)
    pygame.draw.line(display, (0, 0, 255), (width/2, height/2), hand_end(150, minute_angle), 2)
    pygame.draw.line(display, (0, 0, 255), (width/2, height/2), hand_end(100, hour_angle), 5)

    pygame.display.flip()