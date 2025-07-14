import pygame
import sys

# 1. pygame を使う準備
pygame.init()

# 画面サイズ
WIDTH, HEIGHT = 400, 400
# 1マスの大きさ（ピクセル）
CELL_SIZE = 20

# 画面を作る
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake 基礎")

# フレームレート（1秒間に何回画面を描くか）
clock = pygame.time.Clock()

# 2. ヘビの初期状態
# ヘビはセル（正方形）をたくさんつなげたもの
snake = [
    (5, 5),
    (4, 5),
    (3, 5),
]
# 向き：右(1,0)、下(0,1)、左(-1,0)、上(0,-1) のいずれか
direction = (1, 0)

# 3. メインループ
while True:
    # --- イベント処理 ---
    for event in pygame.event.get():
        # ウィンドウの×ボタンで終了
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # キーが押されたら向きを変更
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                direction = (1, 0)
            elif event.key == pygame.K_LEFT:
                direction = (-1, 0)
            elif event.key == pygame.K_UP:
                direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                direction = (0, 1)

    # --- ヘビを動かす ---
    head_x, head_y = snake[0]
    dx, dy = direction
    new_head = (head_x + dx, head_y + dy)
    # 新しい頭をリストの先頭に追加
    snake.insert(0, new_head)
    # シンプル骨格なので、後ろ（尻尾）は消して長さを変えない
    snake.pop()

    # --- 画面を塗りつぶし（背景）---
    screen.fill((0, 0, 0))  # 黒

    # --- ヘビを描く ---
    for x, y in snake:
        rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (0, 255, 0), rect)  # 緑の四角

    # --- 画面更新 ---
    pygame.display.flip()

    # --- 次のフレームまで少し待つ ---
    clock.tick(10)  # 1秒間に10回更新（スピード調整）
