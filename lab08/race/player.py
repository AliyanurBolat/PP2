import pygame

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SPEED = 5

class Player:
    def __init__(self):
        self.WIDTH = 60
        self.ASPECT_RATIO = 0.5
        self.height = self.WIDTH / self.ASPECT_RATIO
        self.image = pygame.image.load("images/cars/car_yellow.png")
        self.image = pygame.transform.scale(self.image, (self.WIDTH, self.height))
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
        self.MOVE_SPEED = SPEED * 3
        
    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            if(self.rect.left > 0):
               self.rect.move_ip(-self.MOVE_SPEED, 0)
        if keys[pygame.K_RIGHT]:
            if(self.rect.right < SCREEN_WIDTH):
               self.rect.move_ip(self.MOVE_SPEED, 0)

           
    def draw(self, screen):
        screen.blit(self.image, self.rect)
