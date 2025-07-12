import pygame
import sys

def main():
    # ───── 定数設定 ─────
    # 画面
    WIDTH, HEIGHT = 640, 480
    FPS = 60

    # 色
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)

    # パドル
    PADDLE_WIDTH, PADDLE_HEIGHT = 10, 100
    PADDLE_SPEED = 5
    PADDLE_OFFSET = 20  # 画面端からの距離

    # ボール
    BALL_RADIUS = 8
    BALL_SPEED_X = 4
    BALL_SPEED_Y = 4

    # ───── pygame 初期化 ─────
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pong 基礎（ブラッシュアップ版）")
    clock = pygame.time.Clock()

    # ───── オブジェクト初期配置 ─────
    paddle = pygame.Rect(
        PADDLE_OFFSET,
        (HEIGHT - PADDLE_HEIGHT) // 2,
        PADDLE_WIDTH,
        PADDLE_HEIGHT
    )
    ball = pygame.Rect(0, 0, BALL_RADIUS*2, BALL_RADIUS*2)
    ball.center = (WIDTH // 2, HEIGHT // 2)
    ball_dx = BALL_SPEED_X
    ball_dy = BALL_SPEED_Y

    # ───── ボールを中央に戻す関数 ─────
    def reset_ball():
        nonlocal ball_dx, ball_dy
        ball.center = (WIDTH // 2, HEIGHT // 2)
        # 反対側に向かうようランダムで x 方向を反転
        ball_dx = BALL_SPEED_X * (-1 if ball_dx > 0 else 1)
        ball_dy = BALL_SPEED_Y

    # ───── メイン・ループ ─────
    while True:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # パドル操作（↑↓キー）
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN]:
            paddle.y += PADDLE_SPEED
        # 画面外に出ないように制限
        paddle.y = max(0, min(HEIGHT - PADDLE_HEIGHT, paddle.y))

        # ボール移動
        ball.x += ball_dx
        ball.y += ball_dy

        # 壁（上下端）で跳ね返し
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_dy = -ball_dy

        # パドルとの衝突判定
        if ball.colliderect(paddle):
            ball_dx = -ball_dx
            # パドルに埋まらないように位置調整
            ball.left = paddle.right

        # 左右端に逸脱したら中央にリセット
        if ball.left <= 0 or ball.right >= WIDTH:
            reset_ball()

        # ───── 描画 ─────
        screen.fill(BLACK)

        # 中央の破線
        dash_height = 10
        for y in range(0, HEIGHT, dash_height * 2):
            pygame.draw.rect(screen, WHITE, (WIDTH//2 - 1, y, 2, dash_height))

        # パドルとボール
        pygame.draw.rect(screen, WHITE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)

        # 画面更新・フレーム維持
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
