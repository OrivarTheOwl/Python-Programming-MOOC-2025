import pygame
from random import randint, choice

# PNG Info
robot_img = pygame.image.load("robot.png")
monster_img = pygame.image.load("monster.png")
coin_img = pygame.image.load("coin.png")

# Window dimensions
width = 640
height = 480
window = pygame.display.set_mode((width, height))

# Screen borders
left_border = 0
right_border = width
top_border = 0
bottom_border = height



# Robot class for the player character robot
class Robot:
    def __init__(self):
        self.x = width/2-robot_img.get_width()/2
        self.y = height/2-robot_img.get_height()/2
        self.speed = 3
        self.hitbox = pygame.Rect(self.x, self.y, robot_img.get_width(), robot_img.get_height())

        self.up = False
        self.down = False
        self.left = False
        self.right = False

    # Robot movement logic
    def movement(self):
        if self.up and self.y >= top_border:
            self.y -= self.speed
        if self.down and self.y <= bottom_border-robot_img.get_height():
            self.y += self.speed
        if self.left and self.x >= left_border:
            self.x -= self.speed
        if self.right and self.x <= right_border-robot_img.get_width():
            self.x += self.speed



# Class to simulate monster enemies
class Monster:
    def __init__(self):
        self.direction = choice(["top", "bottom", "left", "right"])
        #self.direction = choice(["top", "top", "top", "top"])
        self.x, self.y = self.which_direction(self.direction)
        self.speed = 5
        self.hitbox = pygame.Rect(self.x, self.y, monster_img.get_width(), monster_img.get_height())
        self.offscreen = False

    # Method to set starting position
    def which_direction(self, direction: str):
        match direction:
            case "top":
                x = randint(left_border, right_border-monster_img.get_width())
                y = randint(0-height*2, top_border-100)
                return x, y
            case "bottom":
                x = randint(left_border, right_border-monster_img.get_width())
                y = randint(bottom_border+100, height*2)
                return x, y
            case "left":
                x = randint(0-width*2, left_border-100)
                y = randint(top_border, bottom_border-monster_img.get_height())
                return x, y
            case "right":
                x = randint(right_border+100, width*2)
                y = randint(top_border, bottom_border-monster_img.get_height())
                return x, y

    # Method to cause movement in specified direction
    def movement(self):
        if self.direction == "top":
            self.y += self.speed
        elif self.direction == "bottom":
            self.y -= self.speed
        elif self.direction == "left":
            self.x += self.speed
        elif self.direction == "right":
            self.x -= self.speed



# Class for a coin that provides an extra point each wave if collected
class Coin:
    def __init__(self):
        self.x = randint(left_border, right_border-coin_img.get_width())
        self.y = randint(top_border, bottom_border-coin_img.get_height())
        self.hitbox = pygame.Rect(self.x, self.y, coin_img.get_width(), coin_img.get_height())



# Main game class that runs everything
class Game:
    def __init__(self):
        pygame.init()

        self.robot = Robot()
        self.monsters = []
        self.monster_count = 1
        self.coin = None

        self.wave_number = 0
        self.score = -1
        self.game_over = False

        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont("Arial", 24)
        pygame.display.set_caption("Monster Invasion")

        self.spawn_wave()

        self.main_loop()

    # Main loop that continuously runs
    def main_loop(self):
        while True:
            self.check_events()
            
            if not self.game_over:
                self.robot.movement()
                for monster in self.monsters:
                    monster.movement()

                self.update_hitboxes()
                self.collision_check()

                if self.offscreen_check():
                    self.spawn_wave()

            self.draw_window()
            self.clock.tick(60)

    # Spawns the next wave of monsters
    def spawn_wave(self):
        for i in range(self.monster_count):
            monster = Monster()
            self.monsters.append(monster)
        self.monster_count += 1
        self.wave_number += 1
        self.score += 1
        self.coin = Coin()

    # Checks to see if all monsters are far past the screen borders
    def offscreen_check(self):
        all_offscreen = True
        for monster in self.monsters:
            if (monster.x < -1000 or monster.x > 1000) or (monster.y < -1000 or monster.y > 1000):
                monster.offscreen = True
            else:
                monster.offscreen = False
                all_offscreen = False
        return all_offscreen
    
    # Keeps object hitboxes aligned with sprites
    def update_hitboxes(self):
        self.robot.hitbox.topleft = (self.robot.x, self.robot.y)
        for monster in self.monsters:
            monster.hitbox.topleft = (monster.x, monster.y)
            # Also makes the monster hitbox a little bit smaller
            monster.shrunk_hitbox = monster.hitbox.inflate(-20, -20)
        if self.coin:
            self.coin.hitbox.topleft = (self.coin.x, self.coin.y)

    # Checks for collision between objects
    def collision_check(self):
        for monster in self.monsters:
            if self.robot.hitbox.colliderect(monster.shrunk_hitbox):
                self.game_over = True
        if self.coin and self.robot.hitbox.colliderect(self.coin.hitbox):
            self.score += 1
            self.coin = None


    # Check for events every frame
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

            # Robot movement checks
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.robot.up = True
                if event.key == pygame.K_DOWN:
                    self.robot.down = True
                if event.key == pygame.K_LEFT:
                    self.robot.left = True
                if event.key == pygame.K_RIGHT:
                    self.robot.right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    self.robot.up = False
                if event.key == pygame.K_DOWN:
                    self.robot.down = False
                if event.key == pygame.K_LEFT:
                    self.robot.left = False
                if event.key == pygame.K_RIGHT:
                    self.robot.right = False

    # Draw visuals on screen every frame
    def draw_window(self):
        window.fill((100, 120, 200))
        total_score = self.game_font.render(f"Points: {self.score}", True, (255, 0, 0))
        wave_count = self.game_font.render(f"Wave: {self.wave_number}", True, (255, 0, 0))
        window.blit(total_score, (125, 450))
        window.blit(wave_count, (5, 450))

        window.blit(robot_img, (self.robot.x, self.robot.y))
        for monster in self.monsters:
            window.blit(monster_img, (monster.x, monster.y))
        if self.coin:
            window.blit(coin_img, (self.coin.x, self.coin.y))

        if self.game_over:
            game_over = self.game_font.render(f"Game Over", True, (255, 0, 0))
            final_score = self.game_font.render(f"Final Score: {self.score}", True, (255, 0, 0))
            window.blit(game_over, (260, 190))
            window.blit(final_score, (250, 220))
        pygame.display.flip()



if __name__ == "__main__":
    Game()