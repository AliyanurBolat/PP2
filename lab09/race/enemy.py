import pygame 
import random
import os

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SPEED = 5

class Enemy:
    def __init__(self):
        self.WIDTH = 60
        self.ASPECT_RATIO = 0.5
        colors = os.listdir("images/cars")
        self.height = self.WIDTH / self.ASPECT_RATIO
        self.image = pygame.image.load("images/cars/" + random.choice(colors))
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.height))
        self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.center = self.random_position()
        self.speed = SPEED
        
    def random_position(self):
        y = int(-self.height)
        x = random.randint(10, SCREEN_WIDTH - 10 - self.rect.width)
        return x, y
    
    def speed_change(self, speed):
        self.speed += speed
        
        
    def move(self):
        self.rect.move_ip(0, self.speed)
        if(self.rect.top > SCREEN_HEIGHT):
          self.__init__()
          
    def draw(self, screen):
        screen.blit(self.image, self.rect)