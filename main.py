import pygame, sys
from pygame.locals import *
from setting.setting import *
from function import *
from screen.mainScreen import *

pygame.init()
FPS_control = pygame.time.Clock()
ticks = pygame.time.get_ticks()

screen = pygame.display.set_mode((screen_width, screen_height))
setting = Setting()
main_screen = MainScreen(setting, ticks)

while True:
    ticks = pygame.time.get_ticks()
    mouse_position = pygame.mouse.get_pos()
    get_event(setting, main_screen, mouse_position, ticks)
    
    main_screen.update(setting, ticks)

    main_screen.draw(screen, setting)

    FPS_control.tick(FPS)
    pygame.display.update()