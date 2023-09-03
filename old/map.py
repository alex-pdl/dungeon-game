import pygame
from classes import Tile, Player
level = [
'NNN                      NNNNNNNNNNN',
'NNN                      NNNNNNNNNNN',
'NNN                      NNNNNNNNNNN',
'NNN                      NNNNNNNNNNN',
'NNN           NNNNNNNNNNNNNNNNNNNNNN',
'NNN     NN    NNNNNNNNNNNNNNNNNNNNNN',
'NNN           NNNNNNNNNNNNNNNNNNNNNN',
'NNN           NTNNNNNNNNNNNNNNNNNNNN',
'NNN           NNNNNNNNNNNNNNNNNNNNNN',
'NNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNN',
]

tile_size = 48
player = pygame.sprite.GroupSingle()
player.add(Player())
world_shift = 1

def scroll_x():
    global world_shift
    if player.sprite.rect.centerx < 200:
        if player.sprite.direction.x < 0:
            world_shift += 8
            player.sprite.speed = 0
    elif player.sprite.rect.centerx > 580:
        if player.sprite.direction.x > 0:
            world_shift += -8
            player.sprite.speed = 0
    else:
        world_shift = 0

def map(level_info,surface):
    global tiles
    tiles = pygame.sprite.Group()
    global speed
    speed = 5
    #rendering the tiles on the screen
    for row_index,row in enumerate(level_info):
        for column_index,column in enumerate(row):
            if column != " ":
                x = column_index*tile_size
                y = row_index*tile_size
                tile = Tile(column,(x,y))
                tiles.add(tile)

    player.sprite.rect.x += player.sprite.direction.x * speed
    #stops player from moving into tile horizontally
    for sprite in tiles.sprites():
        if sprite.rect.colliderect(player.sprite.rect):
            print(True)
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
    tiles.update(world_shift)
    tiles.draw(surface)
    scroll_x()
    print(player.sprite.rect.centerx)

