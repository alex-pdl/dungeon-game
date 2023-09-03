import pygame
import random
screen_width = 720
screen_height = 480

class Enemy(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        
        # Load the enemy image (replace 'enemy_image.png' with your image file)
        self.image = pygame.image.load('cat_left.png')
        self.rect = self.image.get_rect()

        # Set the initial position of the enemy randomly on the screen
        self.rect.x = random.randint(0, screen_width - self.rect.width)
        self.rect.y = random.randint(0, screen_height - self.rect.height)

        # Set the speed of the enemy (adjust as needed)
        self.speed = random.randint(1, 3)

    def update(self):
        # Move the enemy downward (you can modify this for different movement patterns)
        self.rect.y += self.speed

        # If the enemy goes off the screen, reset its position to the top
        if self.rect.y > screen_height:
            self.rect.y = -self.rect.height
            self.rect.x = random.randint(0, screen_width - self.rect.width)