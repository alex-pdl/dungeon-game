import pygame
from sys import exit 
#from characters import Player
image = pygame.image.load("assets/sprites/soldier_front.png")

class Player:
    
    def __init__(self,health,bullets,image1,x,y):
        self.health = health
        self.bullets = bullets
        self.x = x
        self.y = y
        self.image1 = image1
        self.rect = self.image1.get_rect(center = (self.x, self.y))
        #default coordinates
        self.x = 280
        self.y = 405
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
        screen.blit(self.image1, (self.x,self.y))

pygame.init()
screen = pygame.display.set_mode((600,450))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()
#font = pygame.font.Font("assets/fonts/Pixeltype.ttf", 50)
map = pygame.image.load("assets/sprites/test_background.png")
player_1 = Player(100,100,image,205,550)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("white")
    screen.blit(map,(0,0))
    player_1.movement()
    Player.render(player_1)
    #screen.blit(font,(0,0))
    #screen.blit(test, (100,100))

    pygame.display.update()
    clock.tick(60)