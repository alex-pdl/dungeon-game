import pygame
import random
screen_width = 720
screen_height = 480

class Enemy(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.gravity = 1

        # Load the enemy
        self.image = pygame.image.load('assets/sprites/cat/cat_front.png')
        self.rect = self.image.get_rect(topleft = (x,y))
        self.speed = 1

        self.cat_still_front = pygame.image.load("assets/sprites/cat/cat_front.png")
        self.cat_still_left = pygame.image.load("assets/sprites/cat/cat_left_still.png")
        self.cat_still_right = pygame.image.load("assets/sprites/cat/cat_right_still.png")
        self.cat_right_move_0 = pygame.image.load("assets/sprites/cat/cat_move_right_1.png")
        self.cat_right_move_1 = pygame.image.load("assets/sprites/cat/cat_move_right_0.png")
        self.cat_left_move_0 = pygame.image.load("assets/sprites/cat/cat_left_move_1.png")
        self.cat_left_move_1 = pygame.image.load("assets/sprites/cat/cat_left_move_0.png")

        self.cat_right_move = [self.cat_right_move_0,self.cat_still_right,self.cat_right_move_1]
        self.cat_right_move_index = 0
        self.cat_left_move = [self.cat_left_move_0,self.cat_still_left,self.cat_left_move_1]
        self.cat_left_move_index = 0
        self.direction = pygame.math.Vector2(x,y)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def animation_state(self):
        if self.direction.x >= 1:
            #right
            self.image = self.cat_still_right
            self.cat_right_move_index += 1
            if self.cat_right_move_index >= 3:
                self.cat_right_move_index = 0
            self.image = self.cat_right_move[self.cat_right_move_index]

        elif self.direction.x <= -1:
            #left
            self.image = self.cat_still_left
            self.cat_left_move_index += 1
            if self.cat_left_move_index >= 3:
                self.cat_left_move_index = 0
            self.image = self.cat_left_move[self.cat_left_move_index]

        # Set the initial position of the enemy randomly on the screen
        #self.rect.x = random.randint(0, 2000)
        #self.rect.y = random.randint(0, 0)
        # Set the speed of the enemy (adjust as needed)

    def update(self):
        # Move the enemy downward (you can modify this for different movement patterns)
        self.rect.x += self.speed
        self.animation_state()
        self.apply_gravity()

        # If the enemy goes off the screen, reset its position to the top
        if self.rect.y > screen_height:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, screen_width - self.rect.width)