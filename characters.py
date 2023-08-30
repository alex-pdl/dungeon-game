import pygame

class Player:
    x = 205
    y = 550 
    def __init__(self,health,bullets,image):
        self.health = health
        self.bullets = bullets
        self.image_ren = pygame.image.load(image)
        self.rect = self.image_ren.get_rect()

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 5
        if keys[pygame.K_a]:
            self.x -= 5
        if keys[pygame.K_s]:
            self.y += 5
        if keys[pygame.K_d]:
            self.x += 5
    
    def render(self):
        screen.blit(self.image_ren, self.rect)

