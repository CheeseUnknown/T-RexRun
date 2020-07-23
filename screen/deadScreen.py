import pygame, random
from pygame.locals import *
from setting.setting import *

class DeadScreen(object):
    def __init__(self):
        self.load()

    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)
        self.image.blit(dead_screen_game_over_image, (259.5, 90.5))

    def load(self):
        self.load_image()
        self.x = 0
        self.y = 0

    def update(self):
        self.load_image()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))