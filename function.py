import pygame, sys
from pygame.locals import *
from setting.setting import *

def get_event(setting, main_screen, mouse_position, ticks):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit(0)
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                sys.exit(0)
        if setting.table == 0:
            if event.type == MOUSEBUTTONDOWN:
                setting.table = 1
        elif setting.table == 1:
            if event.type == MOUSEBUTTONDOWN:
                setting.mouse_pressed = True
            elif event.type == MOUSEBUTTONUP:
                setting.mouse_pressed = False
        elif setting.table == 2:
            if event.type == MOUSEBUTTONUP:
                if mouse_position[0] >= 349.5 and mouse_position[0] <= 384.5 and mouse_position[1] >= 156.5 and mouse_position[1] <= 182.5:
                    setting.table = 1
                    main_screen.playing_screen.load(setting, ticks)
    if not main_screen.playing_screen.TRex_group_single.sprite.is_jumping:
        if setting.mouse_pressed:
            main_screen.playing_screen.TRex_group_single.sprite.is_jumping = True
            main_screen.playing_screen.TRex_group_single.sprite.velocity = -4.3
            jump_sound.play()
                
def write_txt(setting):
    with open("setting/setting.txt", "r") as f:
        lines = f.readlines()
    with open('setting/setting.txt', "w") as f:
        for line in lines:
            if "bestscore:" in line:
                line = "bestscore:" + str(setting.best_score)
            f.write(line)

def print_text(screen, font, x, y, text, color):
    text_image = font.render(text, True, color)
    screen.blit(text_image, (x, y))