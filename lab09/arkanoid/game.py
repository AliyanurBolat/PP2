import pygame
from settings import *
import paddle
import ball
import random
from block import Block
from menu import Menu

pygame.init()

def quit_game():
    pygame.quit()
    quit()

def sound():
    global sound_enabled
    sound_enabled = not sound_enabled

def start_game():
    global game_running, score
    game_running = True
    score = 0

def pause():
    global paused
    paused = not paused
    if paused:
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def show_game_over():
    global game_over
    game_over = True

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

background = pygame.image.load('bg.jpg').convert()
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

paddle = paddle.Paddle()
ball = ball.Ball()

blocks = []
for i in range(10):
    for j in range(4):
        block = Block(i * 80 + 2, j * 40 + 10, random.randint(0, len(COLORS) - 1))
        blocks.append(block)

menu = Menu()
menu.append_option('Start Game', start_game)
menu.append_option('Quit', quit_game)

sound_enabled = True
menu.append_option('Sound', sound)

paused = False

game_running = False
game_over = False

while not game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                menu.switch(-1)
            elif event.key == pygame.K_DOWN:
                menu.switch(1)
            elif event.key == pygame.K_RETURN:
                menu.select()

    screen.blit(background,(0, 0))
    menu.draw(screen, 100, 100, 50)

    pygame.display.flip()
    clock.tick(FPS)

if sound_enabled:
    pygame.mixer.music.load('bg.mp3')
    pygame.mixer.music.play(-1)

while game_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause()

    if not paused and not game_over:
        screen.blit(background,(0, 0))
        
        paddle.draw(screen)
        paddle.move()
        
        ball.draw(screen)
        ball.move()
        
        ball.collide_with_blocks(blocks)
        
        for block in blocks:
            if not block.visible:
                score += 1
                blocks.remove(block)
            block.draw(screen)
        
        font = pygame.font.SysFont('comicsansms', 30)
        score_text = font.render(f'Score: {score}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        
        if len(blocks) == 0:
            show_game_over()
        
    pygame.display.flip()
    clock.tick(FPS)

    if game_over:
        while game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        quit_game()

            screen.fill((0, 0, 0))
            font = pygame.font.SysFont('comicsansms', 40)
            lose_text = font.render('END', True, (255, 255, 255))
            screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2 - lose_text.get_height() // 2))
            pygame.display.flip()
            clock.tick(FPS)

        game_running = False
        game_over = False

        while not game_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        menu.switch(-1)
                    elif event.key == pygame.K_DOWN:
                        menu.switch(1)
                    elif event.key == pygame.K_RETURN:
                        menu.select()

            screen.blit(background,(0, 0))
            menu.draw(screen, 100, 100, 50)

            pygame.display.flip()
            clock.tick(FPS)

            if sound_enabled:
                pygame.mixer.music.load('bg.mp3')
                pygame.mixer.music.play(-1)

            blocks = []
            for i in range(10):
                for j in range(4):
                    block = Block(i * 80 + 2, j * 40 + 10, random.randint(0, len(COLORS) - 1))
                    blocks.append(block)

pygame.quit()
