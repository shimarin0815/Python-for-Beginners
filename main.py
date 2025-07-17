# main.py

import pygame, sys
from snake import move_snake, place_food, check_collision

# 初期設定
pygame.init()
CELL = 20
GRID_W, GRID_H = 20, 20
SCREEN = pygame.display.set_mode((CELL*GRID_W, CELL*GRID_H))
CLOCK = pygame.time.Clock()

# 初期データ
snake = [(5,5), (4,5), (3,5)]
direction = (1,0)
food = place_food(snake, (GRID_W, GRID_H))

while True:
    # 1) イベント処理
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_RIGHT: direction=(1,0)
            elif e.key == pygame.K_LEFT:  direction=(-1,0)
            elif e.key == pygame.K_UP:    direction=(0,-1)
            elif e.key == pygame.K_DOWN:  direction=(0,1)

    # 2) 移動・エサ処理
    will_grow = ( (snake[0][0]+direction[0], snake[0][1]+direction[1]) == food )
    snake = move_snake(snake, direction, grow=will_grow)
    if will_grow:
        food = place_food(snake, (GRID_W, GRID_H))

    # 3) 衝突チェック
    if check_collision(snake, (GRID_W, GRID_H)):
        print("ゲームオーバー!")  # デバッグ：コンソールに表示
        break                 # ループを抜けて終了

    # 4) 描画
    SCREEN.fill((0,0,0))
    # ヘビ
    for x,y in snake:
        pygame.draw.rect(SCREEN, (0,255,0), (x*CELL,y*CELL,CELL,CELL))
    # エサ
    fx,fy = food
    pygame.draw.rect(SCREEN, (255,0,0), (fx*CELL,fy*CELL,CELL,CELL))

    pygame.display.flip()
    CLOCK.tick(10)
