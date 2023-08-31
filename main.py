import pygame
from sys import exit 
from characters import Player

pygame.init()
screen = pygame.display.set_mode((600,450))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()
#font = pygame.font.Font("assets/fonts/Pixeltype.ttf", 50)
map = pygame.image.load("assets/sprites/test_background.png")
player = pygame.sprite.GroupSingle()
player.add(Player(200,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill("white")
    screen.blit(map,(0,0))
    #player_1.movement()
    #Player.render(player_1)
    #screen.blit(font,(0,0))
    #screen.blit(test, (100,100))
    player.draw(screen)
    Player.player_input(player)
    pygame.display.update()
    clock.tick(60)