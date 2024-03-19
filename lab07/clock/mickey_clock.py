import pygame
from datetime import datetime

pygame.init() 
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
CENTER = (SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)

FPS = 60
clock = pygame.time.Clock()

bg = pygame.image.load('images/mickey-clock.jpg')
BG_WIDTH = 500
BG_HEIGHT = 500
BG_X_POS = (SCREEN_WIDTH / 2 - BG_WIDTH / 2)
BG_Y_POS = (SCREEN_HEIGHT / 2 - BG_HEIGHT / 2)

big_arrow = pygame.image.load('images/big-arrow.png')
BIG_ARROW_WIDTH = 35
BIG_ARROW_ASPECT_RATIO = 0.13
BIG_ARROW_HEIGHT = BIG_ARROW_WIDTH / BIG_ARROW_ASPECT_RATIO
big_arrow = pygame.transform.scale(big_arrow, (BIG_ARROW_WIDTH, BIG_ARROW_HEIGHT))

big_arrow_rect = big_arrow.get_rect()
big_arrow_rect.center = CENTER

small_arrow = pygame.image.load('images/small-arrow.png')
SMALL_ARROW_WIDTH = 60
SMALL_ARROW_ASPECT_RATIO = 0.35
SMALL_ARROW_HEIGHT = SMALL_ARROW_WIDTH / SMALL_ARROW_ASPECT_RATIO
small_arrow = pygame.transform.scale(small_arrow, (SMALL_ARROW_WIDTH, SMALL_ARROW_HEIGHT))

small_arrow_rect = small_arrow.get_rect()
small_arrow_rect.center = CENTER

running = True
while running:  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  screen.fill(WHITE)
  screen.blit(bg, (BG_X_POS, BG_Y_POS))
  
  angle = datetime.now().second * -6
  rotated_big_arrow = pygame.transform.rotate(big_arrow, angle)
  rotated_big_arrow_rect = rotated_big_arrow.get_rect()
  rotated_big_arrow_rect.center = big_arrow_rect.center
  screen.blit(rotated_big_arrow, rotated_big_arrow_rect)

  _angle = datetime.now().minute * -6
  rotated_small_arrow = pygame.transform.rotate(small_arrow, _angle)
  rotated_small_arrow_rect = rotated_small_arrow.get_rect()
  rotated_small_arrow_rect.center = small_arrow_rect.center
  screen.blit(rotated_small_arrow, rotated_small_arrow_rect)

  pygame.display.flip()
  clock.tick(FPS)
