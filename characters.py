import pygame

class Player(pygame.sprite.Sprite,x,y):
    def __init__(self):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load("assets/sprites/soldier/soldier_front.png")
        self.rect = self.image.get_rect(midbottom = (self.x,self.y))
    
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 5
        elif keys[pygame.K_s]:
            self.y += 5
        elif keys[pygame.K_a]:
            self.x -= 5
        elif keys[pygame.K_d]:
            self.x += 5