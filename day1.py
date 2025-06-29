import pygame            # ① Pygameの機能を使えるようにする
pygame.init()            # ② Pygameをスタンバイ状態にする

# ③ ウィンドウを作る：横640×縦480
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Day1: Pygame Window")  # ウィンドウのタイトル

running = True           # ゲームを続けるかどうかのフラグ

while running:
    # ④ 「×ボタン」が押されたか調べる
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # ⑤ 画面を真っ黒で塗りつぶす（背景色）
    screen.fill((0, 0, 0))

    # ⑥ 描画した内容を画面に反映
    pygame.display.flip()

# ⑦ Pygameを終了してプログラムをきれいに閉じる
pygame.quit()

