import pygame
from classes import Tile, Player
level = [
'                        ',
'                        ',
'                        ',
'                        ',
'                        ',
'                        ',
'NNNNN       NNNNNNNNNNNN',
'NNMNNCNN    NTNNNNNNNNNN',
'NNNNNNNN    NNNNNNNNNNNN',
'NNNNNNNN    NNNNNNNNNNNN',
'NNNNNNNN    NNNNNNNNNNNN',
'NNNNNNNN    NNNNNNNNNNNN',
]

tile_size = 48
player = pygame.sprite.GroupSingle()
player.add(Player())
def map(level_info,surface):
    global tiles
    tiles = pygame.sprite.Group()
    #rendering the tiles on the screen
    for row_index,row in enumerate(level_info):
        for column_index,column in enumerate(row):
            if column != " ":
                x = column_index*tile_size
                y = row_index*tile_size
                tile = Tile(column,(x,y))
                tiles.add(tile)

    for sprite in tiles.sprites():
        if sprite.rect.colliderect(player.sprite.rect):
            print("True")

    player.draw(surface)
    player.update()
    tiles.draw(surface)
