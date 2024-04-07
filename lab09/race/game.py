import pygame
import player
import enemy
import coin
import math

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
FPS = 60
SPEED = 5
BLACK =(0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.update()

clock = pygame.time.Clock()

running = True

player = player.Player()
enemy = enemy.Enemy()
coin = coin.Coin()

coins = 0
scroll = 0
speed = SPEED

font = pygame.font.SysFont("bahnschrift", 40)

background = pygame.image.load("images/bg.png")
bg_aspect_ratio = background.get_width() / background.get_height()
background = pygame.transform.scale(background, (SCREEN_WIDTH, math.ceil(SCREEN_WIDTH / bg_aspect_ratio)))
copy = math.ceil(SCREEN_HEIGHT / background.get_height()) + 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player.move()
    coin.move()
    enemy.move()
    enemy.speed_change(0.1)
            
    speed += 0.005
    
    scroll = (scroll + speed // 1.5) % background.get_height()
    for x in range(copy):
        screen.blit(background, (0, scroll + (x - 1) * (background.get_height() - 1)))
        
    coin_cnt = font.render(str(coins), True, BLACK)
    pygame.draw.rect(screen, WHITE, (SCREEN_WIDTH - 60, 0, 60, 60))
    screen.blit(coin_cnt, (SCREEN_WIDTH - 50, 10))
  
    player.draw(screen)
    enemy.draw(screen)
    coin.draw(screen)
    
    if(player.rect.colliderect(enemy.rect)):
      screen.fill(RED)
      running = False
    
    if(player.rect.colliderect(coin.rect)):
      coin.__init__()
      coins += 1
      
    if(enemy.rect.colliderect(coin.rect)):
        coin.__init__()
      
    pygame.display.flip()
    clock.tick(FPS)