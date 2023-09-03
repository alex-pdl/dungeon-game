#writing it all again
import pygame,sys
from settings import *
from tiles import Tile
from settings import level_map
from level import Level
from enemy import Enemy

screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
level = Level(level_map,screen)
background = pygame.image.load("assets/background/Untitled.png")
pygame.init()
#game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT
            pygame.quit()
            sys.exit()
    screen.blit(background, (0,0))
    level.run()

    pygame.display.update()
    clock.tick(60)