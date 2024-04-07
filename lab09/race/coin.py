import pygame 
import random

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

SPEED = 5

class Coin:
    def __init__(self):
        self.WIDTH = 20
        self.ASPECT_RATIO = 1
        self.height = self.WIDTH / self.ASPECT_RATIO
        self.image = pygame.image.load("images/coin.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = self.random_position()
        self.MOVE_SPEED = SPEED
        
    def random_position(self):
        y = int(-self.height)
        x = random.randint(10, SCREEN_WIDTH - 10 -self.rect.width)
        return x, y
    
    def move(self):
        self.rect.move_ip(0, self.MOVE_SPEED)
        if(self.rect.top > SCREEN_HEIGHT):
            self.__init__()
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)