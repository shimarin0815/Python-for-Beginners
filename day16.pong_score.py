import pygame
import sys
import random
import os

# ----- 初期化 -----
pygame.init()
try:
    pygame.mixer.init()
except Exception as e:
    print(f"[Warning] pygame.mixer.init() に失敗しました: {e}")

# 画面設定
WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong with Fun Scoring")

# フレームレート、フォント、勝利スコア
FPS = 60
FONT = pygame.font.Font(None, 74)
WINNING_SCORE = 5

# 色定義
BG_COLOR     = (30,  30,  30)
LINE_COLOR   = (200, 200, 200)
PADDLE_COLOR = (240, 240, 240)
BALL_COLOR   = (255, 100, 100)
SCORE_COLOR  = (255, 220, 0)

# 効果音ロード
sound_dir  = os.path.dirname(os.path.abspath(__file__))
hit_file   = os.path.join(sound_dir, "hit.wav")
score_file = os.path.join(sound_dir, "score.wav")

try:
    HIT_SOUND = pygame.mixer.Sound(hit_file)
except Exception as e:
    print(f"[Error] hit.wav をロードできませんでした: {e}")
    HIT_SOUND = None

try:
    SCORE_SOUND = pygame.mixer.Sound(score_file)
except Exception as e:
    print(f"[Error] score.wav をロードできませんでした: {e}")
    SCORE_SOUND = None

# パーティクルリスト
particles = []

class Paddle:
    def __init__(self, x, y):
        self.rect  = pygame.Rect(x, y, 10, 100)
        self.speed = 5

    def move(self, up=True):
        self.rect.y += -self.speed if up else self.speed
        self.rect.y = max(0, min(self.rect.y, HEIGHT - self.rect.height))

    def draw(self, win):
        pygame.draw.rect(win, PADDLE_COLOR, self.rect, border_radius=5)

class Ball:
    def __init__(self):
        self.rect      = pygame.Rect(WIDTH//2 - 15, HEIGHT//2 - 15, 30, 30)
        self.speed_x   = 4
        self.speed_y   = 4

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.speed_y *= -1

    def draw(self, win):
        pygame.draw.ellipse(win, BALL_COLOR, self.rect)

    def reset(self):
        self.rect.center = (WIDTH//2, HEIGHT//2)
        self.speed_x   *= -1

def create_particles(x, y):
    for _ in range(20):
        vx = random.uniform(-2, 2)
        vy = random.uniform(-2, 2)
        r  = random.randint(2, 4)
        particles.append([[x, y], [vx, vy], r])

def update_particles(win):
    for p in particles[:]:
        pos, vel, rad = p
        pos[0] += vel[0]
        pos[1] += vel[1]
        rad    -= 0.1
        if rad <= 0:
            particles.remove(p)
        else:
            pygame.draw.circle(win, SCORE_COLOR, (int(pos[0]), int(pos[1])), int(rad))

def draw(win, paddles, ball, score_l, score_r):
    win.fill(BG_COLOR)
    pygame.draw.line(win, LINE_COLOR, (WIDTH//2, 0), (WIDTH//2, HEIGHT), 2)
    for p in paddles:
        p.draw(win)
    ball.draw(win)

    left_surf  = FONT.render(str(score_l), True, SCORE_COLOR)
    right_surf = FONT.render(str(score_r), True, SCORE_COLOR)
    win.blit(left_surf,  (WIDTH//4  - left_surf.get_width()//2, 20))
    win.blit(right_surf, (WIDTH*3//4 - right_surf.get_width()//2, 20))

    update_particles(win)
    pygame.display.flip()

def main():
    clock        = pygame.time.Clock()
    left_paddle  = Paddle(10, HEIGHT//2 - 50)
    right_paddle = Paddle(WIDTH - 20, HEIGHT//2 - 50)
    ball         = Ball()
    score_l, score_r = 0, 0

    print("ゲームを開始します。")
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("ゲームを終了します。")
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:    left_paddle.move(True)
        if keys[pygame.K_s]:    left_paddle.move(False)
        if keys[pygame.K_UP]:   right_paddle.move(True)
        if keys[pygame.K_DOWN]: right_paddle.move(False)

        ball.move()
        if ball.rect.colliderect(left_paddle.rect) or ball.rect.colliderect(right_paddle.rect):
            ball.speed_x *= -1
            if HIT_SOUND: HIT_SOUND.play()
            create_particles(ball.rect.centerx, ball.rect.centery)

        if ball.rect.left <= 0:
            score_r += 1
            if SCORE_SOUND: SCORE_SOUND.play()
            create_particles(ball.rect.left, ball.rect.centery)
            ball.reset()
        if ball.rect.right >= WIDTH:
            score_l += 1
            if SCORE_SOUND: SCORE_SOUND.play()
            create_particles(ball.rect.right, ball.rect.centery)
            ball.reset()

        draw(WIN, [left_paddle, right_paddle], ball, score_l, score_r)

        if score_l >= WINNING_SCORE or score_r >= WINNING_SCORE:
            result = "YOU WIN!" if score_l > score_r else "YOU LOSE..."
            msg    = FONT.render(result, True, SCORE_COLOR)
            WIN.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - msg.get_height()//2))
            pygame.display.flip()
            pygame.time.delay(3000)
            break

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
