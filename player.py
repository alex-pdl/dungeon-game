import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((35,75))
        self.image.fill("blue")
        self.rect = self.image.get_rect(topleft = pos)