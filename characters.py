import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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