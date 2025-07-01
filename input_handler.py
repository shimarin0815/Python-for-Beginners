# input_handler.py

import pygame
import logging

logger = logging.getLogger(__name__)

def handle_input():
    """
    ユーザー入力を扱い、
    - 終了シグナル (running: bool)
    - 入力データ辞書 (keys, mouse_pos, mouse_buttons)
    を返す。
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            logger.debug("QUITイベント検知")
            return False, {}
        # 必要あればキー押下／離上のイベントハンドリングを追加

    keys = pygame.key.get_pressed()
    mouse_pos = pygame.mouse.get_pos()
    mouse_buttons = pygame.mouse.get_pressed()
    logger.debug(f"keys={keys}, mouse_pos={mouse_pos}, mouse_buttons={mouse_buttons}")
    return True, {
        'keys': keys,
        'mouse_pos': mouse_pos,
        'mouse_buttons': mouse_buttons
    }
