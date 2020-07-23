import pygame, random
from pygame.locals import *
from setting.setting import *
from sprite.TRex import *
from sprite.cloud import *
from sprite.cactus import *
from function import *

class PlayingScreen(object):
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
        self.cloud_group = pygame.sprite.Group()
        self.cactus_group = pygame.sprite.Group()
        cactus = Cactus()
        self.cactus_group.add(cactus)

    def update(self, setting, ticks, screen):
        self.load_image()
        self.cloud_manager()
        self.cactus_manager()
        self.TRex_group_single.update(setting, ticks)
        self.die(setting, screen)

    def draw(self, screen):
        self.TRex_group_single.draw(self.image)
        self.cloud_group.draw(self.image)
        self.cactus_group.draw(self.image)
        screen.blit(self.image, (self.x, self.y))

    def cloud_manager(self):
        x = random.randint(0, 200)
        self.cloud_group.update()
        if x == 0:
            cloud0 = Cloud()
            self.cloud_group.add(cloud0)
            for cloud in self.cloud_group:
                if cloud.x <= -41:
                    self.cloud_group.remove(cloud)

    def cactus_manager(self):
        self.cactus_group.update()
        for cactus in self.cactus_group:
            if cactus.is_last:
                if cactus.x < 600:
                    x = random.randint(0, 150)
                    if x == 0:
                        cactus.is_last = False
                        cactus0 = Cactus()
                        self.cactus_group.add(cactus0)

    def die(self, setting, screen):
        if pygame.sprite.spritecollide(self.TRex_group_single.sprite, self.cactus_group, False, pygame.sprite.collide_mask):
            die_sound.play()
            setting.table = 2
            self.TRex_group_single.sprite.image = TRex_image[3]
            self.draw(screen)
            if setting.score > setting.best_score:
                setting.best_score = setting.score
                write_txt(setting)
            setting.score = 0