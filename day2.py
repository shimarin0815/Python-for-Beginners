import pygame           # ① Pygame を使えるようにする
pygame.init()           # ② Pygame の準備完了

# ③ ウィンドウ（キャンバス）を作成：幅640×高さ480
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Day2: 図形描画")

running = True          # ループを続けるためのスイッチ

while running:
    # ④ イベント処理：×ボタンが押されたら終了
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ⑤ 背景色を水色で塗りつぶす（RGB=(135,206,235)）
    screen.fill((135, 206, 235))

    # ⑥ 赤い四角形を描く
    #    pygame.draw.rect(画面, 色, (x, y, 幅, 高さ))
    pygame.draw.rect(
        screen,
        (255, 0, 0),         # 赤色
        (100, 100, 200, 150) # 左上(100,100) 幅200×高さ150
    )

    # ⑦ 緑の円を描く
    #    pygame.draw.circle(画面, 色, (中心x, 中心y), 半径)
    pygame.draw.circle(
        screen,
        (0, 255, 0),         # 緑色
        (400, 300),          # 中心座標(400,300)
        75                   # 半径75ピクセル
    )

    # ⑧ 描画した内容を画面に反映
    pygame.display.flip()

# ⑨ Pygame を終了してウィンドウを閉じる
pygame.quit()
