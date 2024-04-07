import pygame
from settings import *

class Block:
    def __init__(self, x, y, color_index):
        self.rect = pygame.Rect(x, y, BLOCK_W, BLOCK_H)
        self.color = COLORS[color_index]
        self.visible = True
        
    def draw(self, screen):
        if self.visible:
            pygame.draw.rect(screen, self.color, self.rect)
