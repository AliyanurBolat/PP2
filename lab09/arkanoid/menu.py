import pygame
from settings import *

class Menu:
    def __init__(self):
        pygame.init()
        self.font = pygame.font.SysFont('comicsansms', FONT_SIZE)
        self.option_surfaces = []
        self.callbacks = []
        self.current_option_index = 0
        
    def append_option(self, option, callback):
        self.option_surfaces.append(self.font.render(option, True, DARK_BLUE))
        self.callbacks.append(callback)
        
    def switch(self, direction):
        self.current_option_index = max(0, min(self.current_option_index + direction, len(self.option_surfaces) - 1))
    
    def select(self):
        self.callbacks[self.current_option_index]()
        
    def draw(self, surf, x, y, option_y_padding):
        for i, option in enumerate(self.option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self.current_option_index:
                pygame.draw.rect(surf, LIGHT_BLUE, option_rect)
            surf.blit(option, option_rect)
