import pygame
import random
import sys

# --- 定数設定 ---
WIDTH, HEIGHT = 800, 600
BG_COLOR = (30, 30, 30)
FPS = 60
INIT_CIRCLES = 10
FONT_SIZE_SCORE = 36

class Circle:
    def __init__(self):
        self.radius = random.randint(20, 50)
        self.x = random.randint(self.radius, WIDTH - self.radius)
        self.y = random.randint(self.radius, HEIGHT - self.radius)
        self.color = (
            random.randint(50, 255),
            random.randint(50, 255),
            random.randint(50, 255)
        )

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (self.x, self.y), self.radius)

    def is_clicked(self, pos):
        dx, dy = pos[0] - self.x, pos[1] - self.y
        return dx*dx + dy*dy <= self.radius*self.radius

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("クリックで消せるランダム円ミニゲーム")
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, FONT_SIZE_SCORE)

    circles = [Circle() for _ in range(INIT_CIRCLES)]
    score = 0

    while True:
        clock.tick(FPS)

        # --- イベント処理 ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = event.pos
                for c in circles:
                    if c.is_clicked(pos):
                        circles.remove(c)
                        score += 1
                        break

        # --- 全消去後の再スタート ---
        if not circles:
            # YOU WIN を1秒表示
            win_surf = font.render("YOU WIN!", True, (255,255,255))
            screen.fill(BG_COLOR)
            screen.blit(win_surf, ((WIDTH-win_surf.get_width())//2, (HEIGHT-win_surf.get_height())//2))
            pygame.display.flip()
            pygame.time.delay(1000)
            circles = [Circle() for _ in range(INIT_CIRCLES)]
            score = 0
            continue

        # --- 描画 ---
        screen.fill(BG_COLOR)
        for circle in circles:
            circle.draw(screen)
        score_surf = font.render(f"Score: {score}", True, (255,255,255))
        screen.blit(score_surf, (10, 10))
        pygame.display.flip()

if __name__ == "__main__":
    main()
