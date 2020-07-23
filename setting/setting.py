import pygame
from pygame.locals import *

pygame.init()
pygame.mixer.init()
FPS = 120
transparent = 0, 0, 0, 0
black = 0, 0, 0
font0 = pygame.font.Font(None, 24)

screen_width = 734
screen_height = 286

main_screen_background = [
    pygame.image.load("image/map0.png"),
    pygame.image.load("image/map1.png"),
]

TRex_image = [
    pygame.image.load("image/long1.png"),
    pygame.image.load("image/long2.png"),
    pygame.image.load("image/long3.png"),#jump
    pygame.image.load("image/over.png"),
]

playing_screen_cloud_image = pygame.image.load("image/yun.png")

cactus_image = [
    pygame.image.load("image/cactus01.png"),
    pygame.image.load("image/cactus02.png"),
    pygame.image.load("image/cactus03.png"),
]

bird = [
    pygame.image.load("image/bird1.png"),
    pygame.image.load("image/bird2.png"),
]

dead_screen_game_over_image = pygame.image.load("image/game_over.png")

jump_sound = pygame.mixer.Sound("sound/jump.mp3")
die_sound = pygame.mixer.Sound("sound/die.mp3")

class Setting(object):
    def __init__(self):
        self.best_score = 0
        with open("setting/setting.txt", "r") as f:
            for line in f.readlines():
                line = line.strip('\n')
                if line.startswith('bestscore:'):
                    self.best_score = int(line.split(":", 1)[1])
        self.score = 0
        # 0:ready 1:playing 2:dead
        self.table = 0
        self.mouse_pressed = False