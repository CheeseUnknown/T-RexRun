import pygame, random
from pygame.locals import *
from setting.setting import *

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load()

    def load_image(self):
        self.image = pygame.Surface((41, 11)).convert_alpha()
        self.image.fill(transparent)
        self.image.blit(playing_screen_cloud_image, (0, 0))

    def load(self):
        self.load_image()
        self.x = 734
        self.y = random.randint(0, 100)
        self.rect = Rect(self.x, self.y, 41, 11)

    def update(self):
        self.load_image()
        self.move()
        self.rect = Rect(self.x, self.y, 41, 11)

    def move(self):
        self.x -= 1