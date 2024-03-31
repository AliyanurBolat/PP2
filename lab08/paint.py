import pygame
import sys

pygame.init()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500

#Colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 105)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Paint")

brush_size = 5
current_color = BLACK

screen.fill(WHITE)

draw = False 
last_pos = None

painting = True

while painting:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                draw = True
                last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: 
                draw = False
                last_pos = None
                
        elif event.type == pygame.MOUSEMOTION:
            if draw:
                if last_pos is not None:
                    pygame.draw.line(screen, current_color, last_pos, event.pos, brush_size)
                last_pos = event.pos
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: # clear all
                screen.fill(WHITE)
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_e:
                current_color = WHITE
            elif event.key == pygame.K_k:
                current_color = BLACK
            elif event.key == pygame.K_y:
                current_color = YELLOW
            elif event.key == pygame.K_UP:
                brush_size += 1
            elif event.key == pygame.K_DOWN:
                if brush_size > 1:
                    brush_size -= 1
                    
    pygame.display.flip()
