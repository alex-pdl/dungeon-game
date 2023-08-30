import pygame
from sys import exit 

pygame.init()
screen = pygame.display .set_mode((480,360))
pygame.display.set_caption("Dungeon game")
clock = pygame.time.Clock()
test_font = pygame.font.Font("/assets/fonts/Pixeltype.ttf", 50)
text_surface = test_font.render("Dungeon", None, "white")
#background_surface = pygame.image.load("")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    #screen.blit(background_surface,(0,0))
    screen.blit(text_surface,(0,0))

    pygame.display.update()
    clock.tick(60)