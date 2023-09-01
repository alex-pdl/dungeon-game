import pygame
from classes import Tile

level = [
'                        ',
'                        ',
'                        ',
'                        ',
'                        ',
'                        ',
'XXXXX       XXXXXXXXXXXX',
'XXXXXXXX    XXXXXXXXXXXX',
'XXXXXXXX    XXXXXXXXXXXX',
'XXXXXXXX    XXXXXXXXXXXX',
'XXXXXXXX    XXXXXXXXXXXX',
'XXXXXXXX    XXXXXXXXXXXX',
]

tile_size = 48
def map(level_info,surface):
    tiles = pygame.sprite.Group()
    for row_index,row in enumerate(level_info):
        for column_index,column in enumerate(row):
            if column != " ":
                x = column_index*tile_size
                y = row_index*tile_size
                tile = Tile(column,(x,y))
                tiles.add(tile)
    tiles.draw(surface)