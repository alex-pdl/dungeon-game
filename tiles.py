import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size,type):
        super().__init__()
        if type == "T":
            self.image = pygame.image.load("assets/sprites/tiles/tile.png")
            self.rect = self.image.get_rect(topleft = pos)
        elif type == "L":
            self.image = pygame.image.load("assets/sprites/tiles/tile_left.png")
            self.rect = self.image.get_rect(topleft = pos)
        elif type == "R":
            self.image = pygame.image.load("assets/sprites/tiles/tile_right.png")
            self.rect = self.image.get_rect(topleft = pos)
    def update(self,x_shift,y_shift):
        self.rect.x += x_shift
        self.rect.y += y_shift