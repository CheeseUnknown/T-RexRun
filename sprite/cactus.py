import pygame, random
from pygame.locals import *
from setting.setting import *

class Cactus(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.load()

    def load_image(self):
        self.image = pygame.Surface((48, 48)).convert_alpha()
        self.image.fill(transparent)
        if self.style == 0:
            self.image.blit(cactus_image[self.style], (0, 9))
        elif self.style == 1:
            self.image.blit(cactus_image[self.style], (13.5, 9))
        elif self.style == 2:
            self.image.blit(cactus_image[self.style], (11, 0))

    def load(self):
        self.style = random.randint(0, 2)
        self.load_image()
        self.x = 734
        self.y = 195
        self.is_last = True
        self.rect = Rect(self.x, self.y, 48, 48)

    def update(self):
        self.load_image()
        self.move()
        self.rect = Rect(self.x, self.y, 48, 48)

    def move(self):
        self.x -= 1.8