import pygame
from tiles import Tile
from settings import tile_size
from player import Player

class Level:
    def __init__(self,level_data,surface):
        #setup level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0

    def setup_level(self,layout):
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for column_index,column in enumerate(row):
                if column == "N":
                    x = column_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if column == "S":
                    x = column_index * tile_size
                    y = row_index * tile_size
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)

    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        #player
        self.player.update()
        self.player.draw(self.display_surface)