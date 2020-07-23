import pygame
from pygame.locals import *
from setting.setting import *

class TRex(pygame.sprite.Sprite):
    def __init__(self, setting, ticks):
        pygame.sprite.Sprite.__init__(self)
        self.load(setting, ticks)

    def load_image(self, setting, ticks):
        self.image = pygame.Surface((40, 43)).convert_alpha()
        self.image.fill(transparent)
        if setting.table == 0:
            self.image.blit(TRex_image[2], (0, 0))
        elif setting.table == 1:
            if ticks > self.last_tick + 100:
                setting.score += 2
                self.image_index += 1
                if self.image_index >= 2:
                    self.image_index = 0
                self.last_tick = ticks
            if self.is_jumping:
                self.image.blit(TRex_image[2], (0, 0))
            else:
                self.image.blit(TRex_image[self.image_index], (0, 0))

    def load(self, setting, ticks):
        self.is_jumping = False
        self.velocity = 0
        self.acceleration = 0.12
        self.image_index = 0
        self.last_tick = 0
        self.load_image(setting, ticks)
        self.x = 80
        self.y = 200
        self.rect = Rect(self.x, self.y, 40, 43)

    def update(self, setting, ticks):
        self.load_image(setting, ticks)
        self.jump(setting)
        self.rect = Rect(self.x, self.y, 40, 43)

    def jump(self, setting):
        if setting.table == 1:
            self.velocity += self.acceleration
            self.y += self.velocity
            if self.y >= 200:
                self.is_jumping = False
                self.y = 200