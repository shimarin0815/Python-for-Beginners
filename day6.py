import sys
from typing import Tuple
import pygame

# ----------------------------------------
# 設定 (Constants)
# ----------------------------------------
SCREEN_WIDTH: int = 640
SCREEN_HEIGHT: int = 480
FPS: int = 60

BACKGROUND_COLOR: Tuple[int, int, int] = (30, 30, 30)
BALL_COLOR: Tuple[int, int, int] = (255, 165, 0)

INITIAL_BALL_POS: Tuple[float, float] = (100.0, 100.0)
INITIAL_BALL_SPEED: Tuple[float, float] = (3.0, 2.0)
BALL_RADIUS: int = 20


def update_position(
    pos: pygame.math.Vector2,
    speed: pygame.math.Vector2,
    bounds: Tuple[int, int],
    radius: int
) -> None:
    """
    pos を speed だけ移動させ、bounds 内で跳ね返るように速度を反転させる。

    Args:
        pos: 現在の位置ベクトル
        speed: 速度ベクトル（移動量）
        bounds: (幅, 高さ) のタプル
        radius: オブジェクトの半径
    """
    pos += speed
    width, height = bounds

    # 壁で跳ね返る処理
    if not (radius <= pos.x <= width - radius):
        speed.x *= -1
    if not (radius <= pos.y <= height - radius):
        speed.y *= -1


def main() -> None:
    """
    Pygame を初期化し、ウィンドウを開き、
    ボールを動かすメインループを実行する。
    """
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("変数で管理する Pygame サンプル")
    clock = pygame.time.Clock()

    # 状態の初期化
    ball_pos = pygame.math.Vector2(INITIAL_BALL_POS)
    ball_speed = pygame.math.Vector2(INITIAL_BALL_SPEED)
    radius = BALL_RADIUS

    running = True
    while running:
        # イベント処理
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 位置更新と壁跳ね返り
        update_position(ball_pos, ball_speed, (SCREEN_WIDTH, SCREEN_HEIGHT), radius)

        # 描画
        screen.fill(BACKGROUND_COLOR)
        pygame.draw.circle(
            screen,
            BALL_COLOR,
            (int(ball_pos.x), int(ball_pos.y)),
            radius
        )

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
