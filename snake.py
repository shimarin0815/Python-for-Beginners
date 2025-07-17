# snake.py

import random

# ヘビの動き：頭を移動させて、必要ならしっぽを消す
def move_snake(snake, direction, grow=False):
    """
    snake: [(x,y),…] ヘビの座標リスト
    direction: (dx,dy)
    grow: Trueなら伸ばす（popしない）
    → 新しい座標リストを返す
    """
    head = snake[0]
    new_head = (head[0] + direction[0], head[1] + direction[1])
    new_snake = [new_head] + snake[:]     # 頭だけ先にコピー
    if not grow:
        new_snake.pop()                   # 伸ばさないならしっぽを消す
    return new_snake

# エサをランダムに置く（ヘビと重ならないように）
def place_food(snake, grid_size):
    """
    snake: ヘビの座標
    grid_size: (width_cells, height_cells)
    → (x,y) の座標を返す
    """
    width, height = grid_size
    while True:
        pos = (random.randrange(width), random.randrange(height))
        if pos not in snake:
            return pos

# 衝突判定：壁か自分の体か
def check_collision(snake, grid_size):
    """
    snake: [(x,y),…]
    grid_size: (width_cells, height_cells)
    → 衝突したら True
    """
    head = snake[0]
    x,y = head
    width, height = grid_size
    # 壁
    if x < 0 or x >= width or y < 0 or y >= height:
        return True
    # 自分の体（頭以外）にぶつかった
    if head in snake[1:]:
        return True
    return False
