import pygame
from settings import *

class Paddle:
    def __init__(self):
        self.width = PADDLE_W
        self.height = PADDLE_H
        self.x = SCREEN_WIDTH // 2 - self.width // 2
        self.y = SCREEN_HEIGHT - self.height // 2 - 30
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.movement_speed = SPEED
        
    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            if(self.rect.left > 0):
                self.rect.move_ip(-self.movement_speed, 0)
        if key[pygame.K_RIGHT]:
            if(self.rect.right < SCREEN_WIDTH):
                self.rect.move_ip(self.movement_speed, 0)
                
    def draw(self, screen):
        pygame.draw.rect(screen, DARK_BLUE,self.rect)
    