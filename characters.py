import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        #importing "still" sprites
        self.player_still_front = pygame.image.load("assets/sprites/soldier/soldier_front.png")
        self.player_still_back = pygame.image.load("assets/sprites/soldier/soldier_back.png")
        self.player_still_left = pygame.image.load("assets/sprites/soldier/soldier_left.png")
        self.player_still_right = pygame.image.load("assets/sprites/soldier/soldier_right.png")
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
        self.player_right_move = [player_right_move_0,player_front_move_1]
        self.player_right_move_index = 0
        self.player_left_move = [player_left_move_0,player_left_move_1]
        self.player_left_move_index = 0

        self.image = pygame.image.load("assets/sprites/soldier/soldier_front.png")
        self.rect = self.image.get_rect(midbottom = (200,300))
        

    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.rect.y -= 5
        elif keys[pygame.K_s]:
            self.rect.y += 5
        elif keys[pygame.K_a]:
            self.rect.x -= 5
        elif keys[pygame.K_d]:
            self.rect.x += 5

    def update(self):
        self.player_input()