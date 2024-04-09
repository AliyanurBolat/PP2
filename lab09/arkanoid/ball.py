import pygame
import random
from settings import *
import paddle

class Ball:
    def __init__(self):
        self.radius = BALL_RADIUS
        self.ball_rect = int(self.radius * 2 ** 0.5)
        self.first_x = random.randint(self.radius, SCREEN_WIDTH - self.radius)
        self.first_y = SCREEN_HEIGHT // 2
        self.rect = pygame.Rect(self.first_x, self.first_y, self.ball_rect, self.ball_rect)
        self.dx = 1
        self.dy = -1
        
    def move(self):
        self.rect.x += BALL_SPEED * self.dx
        self.rect.y += BALL_SPEED * self.dy

        if self.rect.top < 0:
            self.dy = -self.dy

        if self.rect.left < 0 or self.rect.right > SCREEN_WIDTH:
            self.dx = -self.dx

        if self.rect.bottom > SCREEN_HEIGHT:
            pygame.quit()
            quit()

    def collide_with_paddle(self, paddle):
        if self.rect.colliderect(paddle.rect) and self.dy > 0:
            self.dy = -self.dy
            
    def collide_with_blocks(self, blocks):
        for block in blocks:
            if self.rect.colliderect(block.rect):
                self.dy = -self.dy
                block.visible = False

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.rect.center, self.radius)

