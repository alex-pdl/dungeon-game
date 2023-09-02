import pygame
from classes import Tile, Player
level = [
'N                      N',
'N                      N',
'N                      N',
'N                      N',
'N           NN         N',
'N     NN    NN         N',
'N           NN         N',
'N           NTNNNNNNNNNN',
'N           NNNNNNNNNNNN',
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

    player.sprite.rect.x += player.sprite.direction.x * 5
    #stops player from moving into tile horizontally
    for sprite in tiles.sprites():
        if sprite.rect.colliderect(player.sprite.rect):
            if player.sprite.direction.x < 0:
                player.sprite.rect.left = sprite.rect.right
            elif player.sprite.direction.x > 0:
                player.sprite.rect.right = sprite.rect.left
    
    player.sprite.gravity_apply()
    #stops player from moving into tile vertically
    for sprite in tiles.sprites():
        if sprite.rect.colliderect(player.sprite.rect):
            if player.sprite.direction.y > 0:
                player.sprite.rect.bottom = sprite.rect.top
                player.sprite.direction.y = 0
            elif player.sprite.direction.y < 0:
                player.sprite.rect.top = sprite.rect.bottom
                player.sprite.direction.y = 0

    player.draw(surface)
    player.update()
    tiles.draw(surface)
