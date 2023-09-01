import pygame
import time
from sys import exit 
from classes import *
from map import *

screen_width = 720
screen_height = 480

'''camera_x = 0
camera_y = 0

player_x = screen_width // 2
player_y = screen_height // 2

camera_x = player_x - (screen_width // 2)
camera_y = player_y - (screen_height // 2)
'''
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()


#font = pygame.font.Font("assets/fonts/Pixeltype.ttf", 50)
#loading map and player sprite from Player class

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #rendering map and background on screen
    screen.fill("grey")
    
    #player sprite is drawn and moved/animated on the screen

    '''player.draw(screen)
    player.update()'''
    
    #print(player.sprite.rect.left)
    
    time.sleep(0)
    map(level,screen)
    #for sprite in tiles.sprites():
        #if sprite.rect.colliderect(player.sprite.rect):
            #print(True)
    
    pygame.display.update()
    clock.tick(60)