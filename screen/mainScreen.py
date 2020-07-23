import pygame, random
from pygame.locals import *
from setting.setting import *
from function import *
from screen.readyScreen import *
from screen.playingScreen import *
from screen.deadScreen import *

class MainScreen(object):
    def __init__(self, setting, ticks):
        self.load(setting, ticks)

    def load_image(self):
        self.image = pygame.Surface((screen_width, screen_height)).convert_alpha()
        self.image.fill(transparent)
        self.image.blit(main_screen_background[0], (self.map_x[0], 0))
        self.image.blit(main_screen_background[1], (self.map_x[1], 0))

    def load(self, setting, ticks):
        self.map_x = [0, 734]
        self.load_image()
        self.ready_screen = ReadyScreen(setting, ticks)
        self.playing_screen = PlayingScreen(setting, ticks)
        self.dead_screen = DeadScreen()
        self.x = 0
        self.y = 0
    
    def update(self, setting, ticks):
        self.load_image()
        self.map_move(setting)
        if setting.table == 0:
            self.ready_screen.update(setting, ticks)
        elif setting.table == 1:
            self.playing_screen.update(setting, ticks, self.image)
        elif setting.table == 2:
            self.dead_screen.update()

    def draw(self, screen, setting):
        if setting.table == 0:
            self.ready_screen.draw(self.image)
        elif setting.table == 1:
            self.playing_screen.draw(self.image)
        elif setting.table == 2:
            self.playing_screen.draw(self.image)
            self.dead_screen.draw(self.image)
        print_text(self.image, font0, 5, 5, "HI ", black)
        self.print_score(setting.best_score, 30, 5)
        self.print_score(setting.score, 680, 5)
        screen.blit(self.image, (self.x, self.y))

    def map_move(self, setting):
        if setting.table == 1:
            self.map_x[0] -= 1.8
            self.map_x[1] -= 1.8
            if self.map_x[0] <= -734:
                self.map_x[0] = 734
            elif self.map_x[1] <= -734:
                self.map_x[1] = 734

    def print_score(self, text, x, y):
        text = str(text)
        while len(text) < 5:
            text = '0' + text
        print_text(self.image, font0, x, y, text, black)