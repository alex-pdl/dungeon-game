import pygame
import time
import threading

clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    condition = False
    def __init__(self):
        super().__init__()

        #importing "still" sprites
        self.player_still_front = pygame.image.load("assets/sprites/soldier/soldier_still_front.png")
        self.player_still_back = pygame.image.load("assets/sprites/soldier/soldier_still_back.png")
        self.player_still_left = pygame.image.load("assets/sprites/soldier/soldier_still_left.png")
        self.player_still_right = pygame.image.load("assets/sprites/soldier/soldier_still_right.png")
        #importing sprite for movement animation
        player_front_move_0 = pygame.image.load("assets/sprites/soldier/soldier_front_move_0.png")
        player_front_move_1 = pygame.image.load("assets/sprites/soldier/soldier_front_move_1.png")
        player_back_move_0 = pygame.image.load("assets/sprites/soldier/soldier_back_move_0.png")
        player_back_move_1 = pygame.image.load("assets/sprites/soldier/soldier_back_move_1.png")
        player_right_move_0 = pygame.image.load("assets/sprites/soldier/soldier_right_move_0.png")
        player_right_move_1 = pygame.image.load("assets/sprites/soldier/soldier_right_move_1.png")
        player_left_move_0 = pygame.image.load("assets/sprites/soldier/soldier_left_move_0.png")
        player_left_move_1 = pygame.image.load("assets/sprites/soldier/soldier_left_move_1.png")
        

        
        #creating arrays containing the sprites needed to render animation
        self.player_front_move = [player_front_move_0,player_front_move_1]
        self.player_front_move_index = 0
        self.player_back_move = [player_back_move_0,player_back_move_1]
        self.player_back_move_index = 0
        self.player_right_move = [player_right_move_0,player_right_move_1]
        self.player_right_move_index = 0
        self.player_left_move = [player_left_move_0,player_left_move_1]
        self.player_left_move_index = 0

        self.image = pygame.image.load("assets/sprites/soldier/soldier_still_front.png")
        self.rect = self.image.get_rect(midbottom = (200,300))
        

    def player_input(self):
        speed = 12
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and keys[pygame.K_a]:
            self.rect.x -= speed
            self.rect.y -= speed
        elif keys[pygame.K_w] and keys[pygame.K_d]:
            self.rect.y -= speed 
            self.rect.x += speed
        elif keys[pygame.K_s] and keys[pygame.K_a]:
            self.rect.y += speed
            self.rect.x -= speed
        elif keys[pygame.K_s] and keys[pygame.K_d]:
            self.rect.y += speed
            self.rect.x += speed
        elif keys[pygame.K_w]:
            self.rect.y -= speed
        elif keys[pygame.K_s]:
            self.rect.y += speed
        elif keys[pygame.K_a]:
            self.rect.x -= speed
        elif keys[pygame.K_d]:
            self.rect.x += 10

#Making the sprites change to create a walking animation dependant on direction of movement
    def animation_state(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.image = self.player_still_back
            self.player_back_move_index += 1
            if self.player_back_move_index >= 2:
                self.player_back_move_index = 0
            self.image = self.player_back_move[self.player_back_move_index]
            
        elif keys[pygame.K_s]:
            self.image = self.player_still_front
            self.player_front_move_index += 1
            if self.player_front_move_index >= 2:
                self.player_front_move_index = 0
            self.image = self.player_front_move[self.player_front_move_index]

        elif keys[pygame.K_a]:
            self.image = self.player_still_left
            self.player_left_move_index += 1
            if self.player_left_move_index >= 2:
                self.player_left_move_index = 0
            self.image = self.player_left_move[self.player_left_move_index]
            
        elif keys[pygame.K_d]:
            self.image = self.player_still_right
            self.player_right_move_index += 1
            if self.player_right_move_index >= 2:
                self.player_right_move_index = 0
            self.image = self.player_right_move[self.player_right_move_index]

    def update(self):
        self.player_input()
        self.animation_state()
            
