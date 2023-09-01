import pygame
import time
from sys import exit 
from characters import Player


pygame.init()
screen = pygame.display.set_mode((600,450))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()


#font = pygame.font.Font("assets/fonts/Pixeltype.ttf", 50)
#loading map and player sprite from Player class
map = pygame.image.load("assets/sprites/test_background.png")
player = pygame.sprite.GroupSingle()
player.add(Player())

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #rendering map and background on screen
    screen.fill("white")
    screen.blit(map,(0,0))
    
    #player sprite is drawn and moved/animated on the screen
    player.draw(screen)
    player.update()
    time.sleep(0.07)
    pygame.display.update()
    clock.tick(60)
