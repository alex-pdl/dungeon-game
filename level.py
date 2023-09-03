import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from player import Player

class Level:
    def __init__(self,level_data,surface):
        #setup level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
    def setup_level(self,layout):
        self.player = pygame.sprite.GroupSingle()
        self.tiles = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for column_index,column in enumerate(row):
                x = column_index * tile_size
                y = row_index * tile_size
                if column != " ":
                    if column == "S":
                        player_sprite = Player((x,y))
                        self.player.add(player_sprite)
                    elif column == "M" or column == "N" or column == "T" or column == "C":
                        tile = Tile((x,y),tile_size,column)
                        self.tiles.add(tile)
    def camera_scrollx(self):

        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift_x = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width/4) and direction_x > 0:
            self.world_shift_x = -8
            player.speed = 0
        else:           
            self.world_shift_x = 0
            player.speed = 8


    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
            self.world_shift_x = 0
            player.speed = 8


    
    def horirozontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0

    
    def run(self):
        #level tiles
        self.tiles.update(self.world_shift_x,self.world_shift_y)
        self.tiles.draw(self.display_surface)
        self.camera_scrollx()
        #player
        self.player.update()
        self.player.draw(self.display_surface)
        self.horirozontal_movement_collision()
        self.vertical_movement_collision()  


