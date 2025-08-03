import pygame
from random import randint

pygame.display.set_caption("Asteroids")
pygame.init()

clock = pygame.time.Clock()

# Window dimensions
width = 640
height = 480
window = pygame.display.set_mode((width, height))

# PNG info
robot = pygame.image.load("robot.png")
asteroid_img = pygame.image.load("rock.png")

# Screen borders
left_border = 0
right_border = width
top_border = 0
bottom_border = height

# Asteroid spawning area
x_bound = width-asteroid_img.get_width()
y_bound = (height-asteroid_img.get_height())*2

# Text / points setup
game_font = pygame.font.SysFont("Arial", 24)
points = 0
asteroid_count = 5

# Robot starting position
robot_x = width/2-robot.get_width()/2
robot_y = height-robot.get_height()

# Robot directional logic
left = False
right = False

# Class for asteroid objects
class Asteroid:
    def __init__(self):
        self.x = randint(0, x_bound)
        self.y = randint(0-y_bound*2, 0-asteroid_img.get_height())
        self.speed = 1
        self.update_bounds()

    # Updates the bounds of each asteroid
    def update_bounds(self):
        self.top = self.y
        self.bottom = self.y + asteroid_img.get_height()
        self.left = self.x
        self.right = self.x + asteroid_img.get_width()

# Asteroid creation logic
def spawn_asteroid():
    return Asteroid()
asteroids = [spawn_asteroid() for i in range(asteroid_count)]


# While loop executing actions every frame
while True:

    # Update robot bounds
    robot_top = robot_y
    robot_bottom = robot_y + robot.get_height()
    robot_left = robot_x
    robot_right = robot_x + robot.get_width()

    # Event checks
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
                
        # Movement checks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            if event.key == pygame.K_RIGHT:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            if event.key == pygame.K_RIGHT:
                right = False
    
    # Robot movement logic
    if left and robot_x >= left_border:
        robot_x -= 3
    if right and robot_x <= right_border-robot.get_width():
        robot_x += 3

    # Asteroid movement logic and collision checks
    new_asteroids = []
    for asteroid in asteroids:
        asteroid.y += asteroid.speed
        asteroid.update_bounds()

        # End game if asteroid touches bottom of screen
        if asteroid.bottom >= bottom_border:
            exit()

        # Asteroid collision detection with robot
        if(robot_left <= asteroid.right and
           robot_right >= asteroid.left and
           robot_top <= asteroid.bottom and
           robot_bottom >= asteroid.top): 
            points += 1
            new_asteroids.append(spawn_asteroid())
        else:
            new_asteroids.append(asteroid)

    asteroids = new_asteroids

    # End game if asteroid touches bottom of screen
    for asteroid in asteroids:
        if asteroid.bottom >= bottom_border:
            exit()
            pass

    # Draw static visuals on screen every frame
    window.fill((0, 0, 0))
    text = game_font.render(f"Points: {points}", True, (255, 0, 0))
    window.blit(text, (500, 25))

    # Draw robot and asteroids every frame
    window.blit(robot, (robot_x, robot_y))
    for asteroid in asteroids:
        window.blit(asteroid_img, (asteroid.x, asteroid.y))

    # Display stuff and framerate
    pygame.display.flip()
    clock.tick(60)