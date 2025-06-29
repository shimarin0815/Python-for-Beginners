import pygame

def main():
    # ① Pygame の初期化
    pygame.init()

    # ② 画面サイズとウィンドウタイトル設定
    WIDTH, HEIGHT = 640, 480
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Day3: 図形を動かそう")

    # ③ フレームレート制御用クロックを作成
    clock = pygame.time.Clock()

    # ④ 図形の初期設定
    x, y = 100, 100       # 四角形の左上座標
    SIZE = 50             # 四角形の大きさ
    SPEED = 5             # 移動速度（ピクセル／フレーム）

    running = True
    while running:
        # ─── イベント処理 ───
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # ─── キー入力処理 ───
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            x -= SPEED
        if keys[pygame.K_RIGHT]:
            x += SPEED
        if keys[pygame.K_UP]:
            y -= SPEED
        if keys[pygame.K_DOWN]:
            y += SPEED

        # ─── 画面外に出ないよう範囲チェック ───
        x = max(0, min(x, WIDTH - SIZE))
        y = max(0, min(y, HEIGHT - SIZE))

        # ─── 描画処理 ───
        screen.fill((135, 206, 235))                           # 背景色（水色）で塗りつぶし
        pygame.draw.rect(screen, (255, 0, 0), (x, y, SIZE, SIZE))  # 赤い四角形を描画
        pygame.display.flip()                                   # 裏キャンバス→表キャンバスへ反映

        # ─── フレームレートを 60FPS に制限 ───
        clock.tick(60)

    # ⑤ 終了処理
    pygame.quit()

if __name__ == "__main__":
    main()
