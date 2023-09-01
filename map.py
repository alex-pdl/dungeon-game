import pygame
from classes import Tile

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
def map(level_info,surface):
    
    #rendering the tiles on the screen
    tiles = pygame.sprite.Group()
    for row_index,row in enumerate(level_info):
        for column_index,column in enumerate(row):
            if column != " ":
                x = column_index*tile_size
                y = row_index*tile_size
                tile = Tile(column,(x,y))
                tiles.add(tile)

    tiles.draw(surface)
