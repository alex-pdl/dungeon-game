import pygame
import random
screen_width = 720
screen_height = 480

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        
        # Load the enemy
        self.image = pygame.image.load('assets/sprites/cat/cat_front.png')
        self.rect = self.image.get_rect()

        self.cat_still_front = pygame.image.load("assets/sprites/cat/cat_front.png")
        self.cat_still_left = pygame.image.load("assets/sprites/cat/cat_left_still.png")
        self.cat_still_right = pygame.image.load("assets/sprites/cat/cat_right_still.png")
        self.cat_right_move_0 = pygame.image.load("assets/sprites/cat/cat_move_right1.png")
        self.cat_right_move_1 = pygame.image.load("assets/sprites/cat/cat_move_right0.png")
        self.cat_left_move_0 = pygame.image.load("assets/sprites/cat/cat_left_move1.png")
        self.cat_left_move_1 = pygame.image.load("assets/sprites/cat/cat_left_move0.png")

        self.cat_right_move = [self.cat_right_move_0,self.cat_still_right,self.cat_right_move_1]
        self.cat_right_move_index = 0
        self.cat_left_move = [self.cat_left_move_0,self.cat_still_left,self.cat_left_move_1]
        self.cat_left_move_index = 0
        self.direction = pygame.math.Vector2(0,0)

        def animation_state(self):
            if self.direction.x == 1:
                #right
                self.image = self.cat_still_right
                self.cat_right_move_index += 1
                if self.cat_right_move_index >= 3:
                    self.cat_right_move_index = 0

            elif self.direction.x == -1:
                #left
                self.image = self.cat_still_left
                self.cat_left_move_index += 1
                if self.cat_left_move_index >= 3:
                    self.cat_left_move_index = 0

        # Set the initial position of the enemy randomly on the screen
        self.rect.x = random.randint(0, 2000)
        self.rect.y = random.randint(0, 0)
        # Set the speed of the enemy (adjust as needed)
        self.speed = random.randint(1, 3)

    def update(self):
        # Move the enemy downward (you can modify this for different movement patterns)
        self.rect.y += self.speed

        # If the enemy goes off the screen, reset its position to the top
        if self.rect.y > screen_height:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, screen_width - self.rect.width)