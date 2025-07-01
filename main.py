# main.py

import sys
import logging
import pygame
from config import (
    SCREEN_WIDTH, SCREEN_HEIGHT, MAX_FPS,
    CIRCLE_INITIAL_POS, CIRCLE_RADIUS, MOVE_SPEED
)
from input_handler import handle_input
from renderer import clear_screen, draw_objects, update_display

def init_logging():
    """デバッグ用ログ出力設定"""
    logging.basicConfig(
        level=logging.DEBUG,
        format='[%(asctime)s] %(name)s %(levelname)s: %(message)s',
        datefmt='%H:%M:%S'
    )

def init_pygame():
    """pygame初期化と画面作成"""
    try:
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Day7: 関数化＋モジュール分割 テンプレート v2")
        return screen
    except Exception as e:
        logging.error("pygame初期化失敗", exc_info=e)
        sys.exit(1)

def main():
    init_logging()
    screen = init_pygame()
    clock = pygame.time.Clock()

    # ゲーム状態初期化
    state = {
        'circle_pos': list(CIRCLE_INITIAL_POS),
        'circle_radius': CIRCLE_RADIUS
    }

    running = True
    while running:
        # 経過時間取得（秒）
        dt = clock.tick(MAX_FPS) / 1000.0

        # 1) 入力処理
        running, input_data = handle_input()
        if not running:
            break

        # 2) ロジック更新（delta time対応）
        keys = input_data.get('keys', [])
        dx = dy = 0.0
        if keys[pygame.K_LEFT]:
            dx -= MOVE_SPEED * dt
        if keys[pygame.K_RIGHT]:
            dx += MOVE_SPEED * dt
        if keys[pygame.K_UP]:
            dy -= MOVE_SPEED * dt
        if keys[pygame.K_DOWN]:
            dy += MOVE_SPEED * dt

        state['circle_pos'][0] += dx
        state['circle_pos'][1] += dy

        # 画面端で止める
        x, y = state['circle_pos']
        r = state['circle_radius']
        x = max(r, min(SCREEN_WIDTH - r, x))
        y = max(r, min(SCREEN_HEIGHT - r, y))
        state['circle_pos'] = [x, y]

        # 3) 描画処理
        clear_screen(screen)
        draw_objects(screen, state)
        update_display()

    pygame.quit()

if __name__ == "__main__":
    main()
