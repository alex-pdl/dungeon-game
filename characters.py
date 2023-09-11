import pygame

screen_width = 720
screen_height = 480

class Player(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load("assets/sprites/soldier/soldier_still_right.png")
        self.direction = pygame.math.Vector2(0,0)
        self.rect = self.image.get_rect(topleft = pos)
        
#importing "still" sprites
        self.player_still_front = pygame.image.load("assets/sprites/soldier/soldier_still_front.png")
        self.player_still_back = pygame.image.load("assets/sprites/soldier/soldier_still_back.png")
        self.player_still_left = pygame.image.load("assets/sprites/soldier/soldier_still_left.png")
        self.player_still_right = pygame.image.load("assets/sprites/soldier/soldier_still_right.png")
        #importing sprite for movement animation
        player_front_move_0 = pygame.image.load("assets/sprites/soldier/soldier_front_move_0.png")
        player_front_move_1 = pygame.image.load("assets/sprites/soldier/soldier_front_move_1.png")
        player_back_move_0 = pygame.image.load("assets/sprites/soldier/soldier_back_move_0.png")
        player_back_move_1 = pygame.image.load("assets/sprites/soldier/soldier_back_move_1.png")
        player_right_move_0 = pygame.image.load("assets/sprites/soldier/soldier_right_move_0.png")
        player_right_move_1 = pygame.image.load("assets/sprites/soldier/soldier_right_move_1.png")
        player_left_move_0 = pygame.image.load("assets/sprites/soldier/soldier_left_move_0.png")
        player_left_move_1 = pygame.image.load("assets/sprites/soldier/soldier_left_move_1.png")
        self.player_right_jump = pygame.image.load("assets/sprites/soldier/soldier_right_jump.png")
        self.player_left_jump = pygame.image.load("assets/sprites/soldier/soldier_left_jump.png")
        
        #creating arrays containing the sprites needed to render animation
        self.player_front_move = [player_front_move_0,self.player_still_front,player_front_move_1]
        self.player_front_move_index = 0
        self.player_back_move = [player_back_move_0,self.player_still_back,player_back_move_1]
        self.player_back_move_index = 0
        self.player_right_move = [player_right_move_0,self.player_still_right,player_right_move_1]
        self.player_right_move_index = 0
        self.player_left_move = [player_left_move_0,self.player_still_left,player_left_move_1]
        self.player_left_move_index = 0

        #player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

    def animation_state(self):
        keys = pygame.key.get_pressed()      
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.image = self.player_still_left
            self.player_left_move_index += 1
            if self.player_left_move_index >= 3:
                self.player_left_move_index = 0
            self.image = self.player_left_move[self.player_left_move_index]
            
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.image = self.player_still_right
            self.player_right_move_index += 1
            if self.player_right_move_index >= 3:
                self.player_right_move_index = 0
            self.image = self.player_right_move[self.player_right_move_index]

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_LEFT]:
            self.direction.x = 1
        elif keys[pygame.K_a] or keys[pygame.K_RIGHT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE] and self.direction.y == 0:
            self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        
        self.direction.y = self.jump_speed
    
    def update(self):
        self.input()
        self.animation_state()

class Enemy(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.gravity = 1
        # Load the enemy
        self.image = pygame.image.load('assets/sprites/cat/cat_front.png')
        self.rect = self.image.get_rect(topleft = pos)
        self.speed = 1

        self.cat_still_front = pygame.image.load("assets/sprites/cat/cat_front.png")
        self.cat_still_left = pygame.image.load("assets/sprites/cat/cat_left_still.png")
        self.cat_still_right = pygame.image.load("assets/sprites/cat/cat_right_still.png")
        self.cat_right_move_0 = pygame.image.load("assets/sprites/cat/cat_move_right_1.png")
        self.cat_right_move_1 = pygame.image.load("assets/sprites/cat/cat_move_right_0.png")
        self.cat_left_move_0 = pygame.image.load("assets/sprites/cat/cat_left_move_1.png")
        self.cat_left_move_1 = pygame.image.load("assets/sprites/cat/cat_left_move_0.png")

        self.cat_right_move = [self.cat_right_move_0,self.cat_still_right,self.cat_right_move_1]
        self.cat_right_move_index = 0
        self.cat_left_move = [self.cat_left_move_0,self.cat_still_left,self.cat_left_move_1]
        self.cat_left_move_index = 0

        self.direction = pygame.math.Vector2(x,y)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def animation_state(self):
        if self.direction.x >= 1:
            #right
            self.image = self.cat_still_right
            self.cat_right_move_index += 1
            if self.cat_right_move_index >= 3:
                self.cat_right_move_index = 0
            self.image = self.cat_right_move[self.cat_right_move_index]

        elif self.direction.x <= -1:
            #left
            self.image = self.cat_still_left
            self.cat_left_move_index += 1
            if self.cat_left_move_index >= 3:
                self.cat_left_move_index = 0
            self.image = self.cat_left_move[self.cat_left_move_index]

        # Set the initial position of the enemy randomly on the screen
        #self.rect.x = random.randint(0, 2000)
        #self.rect.y = random.randint(0, 0)
        # Set the speed of the enemy (adjust as needed)

    def update(self):
        # Move the enemy downward (you can modify this for different movement patterns)
        self.rect.x += self.speed
        self.animation_state()
        self.apply_gravity()

        # If the enemy goes off the screen, reset its position to the top
        #if self.rect.y > screen_height:
            #self.rect.y = -self.rect.height
            #self.rect.x = random.randint(0, screen_width - self.rect.width)

class Background(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        pass