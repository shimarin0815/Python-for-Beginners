import pygame
import sys

# 画面サイズ
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
# 残機数
INITIAL_LIVES = 3

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))


def create_blocks(rows, cols, block_width, block_height, gap):
    blocks = pygame.sprite.Group()
    for row in range(rows):
        for col in range(cols):
            x = col * (block_width + gap) + gap
            y = row * (block_height + gap) + gap + 50
            color = (255 - row * 20, row * 20, 150)
            block = Block(x, y, block_width, block_height, color)
            blocks.add(block)
    return blocks

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, radius, color, speed):
        super().__init__()
        self.radius = radius
        self.image = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
        pygame.draw.circle(self.image, color, (radius, radius), radius)
        self.rect = self.image.get_rect(center=(x, y))
        # 浮動小数点位置ベクトル
        self.pos = pygame.math.Vector2(x, y)
        self.velocity = pygame.math.Vector2(speed, -speed)

    def update(self):
        # 位置を浮動小数点で更新
        self.pos += self.velocity
        self.rect.center = (int(self.pos.x), int(self.pos.y))

        # 左右の壁で跳ね返し
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.velocity.x *= -1
        # 上の壁で跳ね返し
        if self.rect.top <= 0:
            self.velocity.y *= -1

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        width = 100
        height = 20
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 128, 0))
        self.rect = self.image.get_rect(midbottom=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 10))
        self.speed = 7

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.x += self.speed


def draw_text(screen, text, x, y, font, color=(0, 0, 0)):
    text_surf = font.render(text, True, color)
    screen.blit(text_surf, (x, y))


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout 基礎 - パドル追加版")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    # ゲーム要素の生成
    blocks = create_blocks(rows=5, cols=10, block_width=70, block_height=20, gap=5)
    ball = Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, radius=10, color=(0, 0, 255), speed=5)
    paddle = Paddle()
    # スプライトグループ
    all_sprites = pygame.sprite.Group(ball, paddle)
    lives = INITIAL_LIVES

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # 更新
        all_sprites.update()

        # ブロックとの衝突判定
        collided = pygame.sprite.spritecollide(ball, blocks, dokill=True)
        if collided:
            ball.velocity.y *= -1

        # パドルとの衝突判定
        if ball.rect.colliderect(paddle.rect):
            ball.velocity.y = -abs(ball.velocity.y)

        # 画面下端での処理
        if ball.rect.bottom >= SCREEN_HEIGHT:
            lives -= 1
            if lives <= 0:
                print("Game Over")
                running = False
            else:
                # ボールを中央にリセット
                ball.pos = pygame.math.Vector2(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
                ball.velocity = pygame.math.Vector2(ball.velocity.x, -abs(ball.velocity.y))

        # 描画
        screen.fill((255, 255, 255))
        blocks.draw(screen)
        all_sprites.draw(screen)
        draw_text(screen, f"Lives: {lives}", 10, 10, font)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
