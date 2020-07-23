import pygame
from pygame.locals import *
from setting.setting import *
from sprite.TRex import *

class ReadyScreen(object):
    def __init__(self, setting, ticks):
        self.load(setting, ticks)

    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)

    def load(self, setting, ticks):
        self.load_image()
        self.x = 0
        self.y = 0
        self.TRex_group_single = pygame.sprite.GroupSingle()
        TR = TRex(setting, ticks)
        self.TRex_group_single.add(TR)

    def update(self, setting, ticks):
        self.load_image()
        self.TRex_group_single.update(setting, ticks)

    def draw(self, screen):
        self.TRex_group_single.draw(self.image)
        screen.blit(self.image, (self.x, self.y))