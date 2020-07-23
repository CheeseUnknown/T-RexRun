import pygame, random
from pygame.locals import *
from setting.setting import *

class Bird(pygame.sprite.Sprite):
    def __init__(self, ticks):
        pygame.sprite.Sprite.__init__(self)
        self.load(ticks)

    def load_image(self, ticks):
        self.image = pygame.Surface((38, 27)).convert_alpha()
        self.image.fill(transparent)
        if ticks > self.last_ticks + 300:
            self.image_index += 1
            if self.image_index >= 2:
                self.image_index = 0
            self.last_ticks = ticks
        self.image.blit(bird[self.image_index], (0, 0))

    def load(self, ticks):
        self.image_index = 0
        self.last_ticks = 0
        self.load_image(ticks)
        self.x = 734
        self.y = random.randint(0, 130)
        self.rect = Rect(self.x, self.y, 38, 27)

    def update(self, ticks):
        self.load_image(ticks)
        self.move()
        self.rect = Rect(self.x, self.y, 38, 27)

    def move(self):
        self.x -= 1.2