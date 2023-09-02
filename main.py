import pygame
import time
from sys import exit 
from classes import *
from map import *

screen_width = 720
screen_height = 480

pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()

#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #rendering map and background on screen
    screen.fill("grey")
    
    time.sleep(0)
    map(level,screen)
    
    pygame.display.update()
    clock.tick(60)