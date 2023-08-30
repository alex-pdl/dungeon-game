import pygame
from sys import exit 
#from characters import Player

class Player:
    
    def __init__(self,health,bullets,image,x,y):
        self.health = health
        self.bullets = bullets
        self.x = x
        self.y = y
        self.image_ren = pygame.image.load(image)
        self.rect = self.image_ren.get_rect()
        
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= 5
            print(self.y)
        if keys[pygame.K_a]:
            self.x -= 5
            print(self.x)
        if keys[pygame.K_s]:
            self.y += 5
            print(self.y)
        if keys[pygame.K_d]:
            self.x += 5
            print(self.x)
    
    def render(self):
        screen.blit(self.image_ren, self.rect.topleft)

pygame.init()
screen = pygame.display.set_mode((600,450))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()
#font = pygame.font.Font("assets/fonts/Pixeltype.ttf", 50)
soldier = pygame.image.load("assets/sprites/soldier_front.png")
map = pygame.image.load("assets/sprites/test_background.png")
player_coordinates = (0,0)
player_1 = Player(100,100,"assets/sprites/soldier_front.png",205,550)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #screen.fill("white")
    screen.blit(map,(0,0))
    player_1.movement()
    player_1.render()
    #screen.blit(font,(0,0))

    pygame.display.update()
    clock.tick(60)