import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height
from characters import Player, Enemy

class Level:
    def __init__(self,level_data,surface):
        #setup level
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift_x = 0
        self.world_shift_y = 0
    def setup_level(self,layout):
        self.cat = pygame.sprite.GroupSingle()
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
                    elif column == "E":
                        cat_sprite = Enemy((x,y))
                        self.cat.add(cat_sprite)
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
    
    def enemy_stationary(self):
        cat = self.cat.sprite
        self.cat_x = cat.rect.centerx
        self.cat_direction_x = cat.direction.x
        #Move the enemy with the map
        if self.world_shift_x == -8:
            self.cat_speed = 8
        elif self.world_shift_x == 8:
            self.cat_speed = 8

            
    def horirozontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        cat = self.cat.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                #horizontal collisions for enemy
                elif cat.direction.x < 0:
                    cat.rect.left = sprite.rect.right
                elif cat.direction.x > 0:
                    cat.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        cat = self.cat.sprite

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
            if sprite.rect.colliderect(cat.rect):
                if cat.direction.y < 0:
                    cat.rect.top = sprite.rect.bottom
                    cat.direction.y = 0
                elif cat.direction.y > 0:
                    cat.rect.bottom = sprite.rect.top
                    cat.direction.y = 0
                
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
        #cat
        self.cat.update()
        self.cat.draw(self.display_surface)
        self.enemy_stationary()