import pygame
import time
import threading

clock = pygame.time.Clock()
class Player(pygame.sprite.Sprite):
    gravity = -9.81
    def __init__(self):
        super().__init__()
        #creating gravity
        self.player_gravity = 0
        
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
        self.player_right_jump = pygame.image.load("assets/sprites/soldier/soldier_right_jump.png")
        self.player_left_jump = pygame.image.load("assets/sprites/soldier/soldier_left_jump.png")
        
        #creating arrays containing the sprites needed to render animation
        self.player_front_move = [player_front_move_0,self.player_still_front,player_front_move_1]
        self.player_front_move_index = 0
        self.player_back_move = [player_back_move_0,self.player_still_back,player_back_move_1]
        self.player_back_move_index = 0
        self.player_right_move = [player_right_move_0,self.player_still_right,player_right_move_1]
        self.player_right_move_index = 0
        self.player_left_move = [player_left_move_0,self.player_still_left,player_left_move_1]
        self.player_left_move_index = 0

        self.image = pygame.image.load("assets/sprites/soldier/soldier_still_front.png")
        self.rect = self.image.get_rect(midbottom = (200,300))

#Making the movement functionality of the soldier
    def player_input(self):
        speed = 13
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= speed
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += speed
#Making the sprites change to create a walking animation dependant on direction of movement
    def animation_state(self):
        keys = pygame.key.get_pressed()
                   
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image = self.player_still_left
            self.player_left_move_index += 1
            if self.player_left_move_index >= 3:
                self.player_left_move_index = 0
            self.image = self.player_left_move[self.player_left_move_index]
            
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.image = self.player_still_right
            self.player_right_move_index += 1
            if self.player_right_move_index >= 3:
                self.player_right_move_index = 0
            self.image = self.player_right_move[self.player_right_move_index]

#making the jump animation depending on direction facing before
        elif keys[pygame.K_SPACE] and self.image == self.player_right_move[0] or keys[pygame.K_SPACE] and self.image == self.player_right_move[1] or keys[pygame.K_SPACE] and self.image == self.player_right_move[2]:
            self.image =  self.player_right_jump
        
        elif keys[pygame.K_SPACE] and self.image == self.player_left_move[0] or keys[pygame.K_SPACE] and self.image == self.player_left_move[1] or keys[pygame.K_SPACE] and self.image == self.player_left_move[2]:
            self.image = self.player_left_jump

    def gravity(self):
        keys = pygame.key.get_pressed()
        self.player_gravity += 1
        self.rect.y += self.player_gravity
        if keys[pygame.K_SPACE]:
            self.player_gravity = -15
        if self.rect.y >210:
            self.rect.y = 210

    def update(self):
        self.player_input()
        self.animation_state()
        self.gravity()

            
class Tile(pygame.sprite.Sprite):
    def __init__(self,type,pos):
        super().__init__()
        if type == "T":
            self.image = pygame.image.load("assets/sprites/tiles/tile_torch.png")
            self.rect = self.image.get_rect(topleft = pos)
        elif type == "N":
            self.image = pygame.image.load("assets/sprites/tiles/tile.png")
            self.rect = self.image.get_rect(topleft = pos)
        elif type == "M":
            self.image = pygame.image.load("assets/sprites/tiles/tile_moss.png")
            self.rect = self.image.get_rect(topleft = pos)
        elif type == "C":
            self.image = pygame.image.load("assets/sprites/tiles/tile_chain.png")
            self.rect = self.image.get_rect(topleft = pos)
        