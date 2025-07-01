# renderer.py

import pygame
from config import BACKGROUND_COLOR, CIRCLE_COLOR

def clear_screen(screen, color=BACKGROUND_COLOR):
    """画面を指定色でクリア"""
    screen.fill(color)

def draw_objects(screen, state):
    """
    ゲームオブジェクトを描画
    state: dict 例{'circle_pos': (x,y), 'circle_radius': r}
    """
    x, y = state['circle_pos']
    radius = state['circle_radius']
    pygame.draw.circle(screen, CIRCLE_COLOR, (int(x), int(y)), radius)

def update_display():
    """描画内容を画面に反映"""
    pygame.display.flip()
