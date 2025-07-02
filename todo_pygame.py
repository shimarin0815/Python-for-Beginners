import os
import sys
import pygame

# ── ファイル I/O 設定 ───────────────────────────
FILENAME, BACKUP_EXT = "tasks.txt", ".bak"

def load_tasks():
    tasks = []
    try:
        if os.path.exists(FILENAME):
            with open(FILENAME, "r", encoding="utf-8") as f:
                tasks = [l.strip() for l in f if l.strip()]
    except IOError as e:
        print(f"❌ 読み込みエラー: {e}")
    return tasks

def save_tasks(tasks):
    try:
        if os.path.exists(FILENAME):
            os.replace(FILENAME, FILENAME + BACKUP_EXT)
        with open(FILENAME, "w", encoding="utf-8") as f:
            for t in tasks:
                f.write(t + "\n")
    except IOError as e:
        print(f"❌ 書き込みエラー: {e}")

# ── Pygame 初期化 ─────────────────────────────────
pygame.init()
pygame.key.start_text_input()  # IME／日本語入力を有効化

WIDTH, HEIGHT = 400, 600
FLAGS = pygame.DOUBLEBUF | pygame.HWSURFACE
screen = pygame.display.set_mode((WIDTH, HEIGHT), FLAGS)
pygame.display.set_caption("To-Do アプリ (Pygame)")

# 日本語対応フォントを明示的に指定
# Windows: "meiryo", macOS: "Hiragino Maru Gothic Pro", Linux: "TakaoPGothic" など
FONT = pygame.font.SysFont("meiryo", 24)

INPUT_RECT = pygame.Rect(10, 10, WIDTH-120, 32)
clock = pygame.time.Clock()

tasks = load_tasks()
input_text = ""
composition_text = ""

running = True
try:
    while running:
        for event in pygame.event.get():
            # 終了イベント
            if event.type == pygame.QUIT:
                running = False

            # IME 編集中テキスト
            elif event.type == pygame.TEXTEDITING:
                composition_text = event.text

            # IME で確定したテキスト
            elif event.type == pygame.TEXTINPUT:
                input_text += event.text
                composition_text = ""

            # Backspace／Enter
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    if composition_text:
                        composition_text = ""
                    else:
                        input_text = input_text[:-1]
                elif event.key == pygame.K_RETURN:
                    if input_text.strip():
                        tasks.append(input_text.strip())
                        save_tasks(tasks)
                        input_text = ""
                        composition_text = ""

            # 左クリックでタスク削除
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                for i in range(len(tasks)):
                    y = 60 + i * 30
                    if pygame.Rect(10, y, WIDTH-20, 28).collidepoint(mx, my):
                        tasks.pop(i)
                        save_tasks(tasks)
                        break

        # ── 描画 ─────────────────────────────────────
        screen.fill((30, 30, 30))
        # 入力欄
        pygame.draw.rect(screen, (200,200,200), INPUT_RECT, 2)
        disp = input_text + composition_text
        screen.blit(FONT.render(disp, True, (255,255,255)),
                    (INPUT_RECT.x+5, INPUT_RECT.y+5))
        screen.blit(FONT.render("Enter: 追加", True, (180,180,180)),
                    (WIDTH-100, 15))
        # タスク一覧
        for i, t in enumerate(tasks):
            y = 60 + i * 30
            pygame.draw.rect(screen, (50,50,50),
                             (10, y, WIDTH-20, 28))
            screen.blit(FONT.render(f"{i+1}. {t}", True, (255,255,255)),
                        (15, y+5))

        pygame.display.flip()
        clock.tick(60)  # 60 FPS でスムーズ表示

except KeyboardInterrupt:
    print("\n⚠️ 中断されました。")

finally:
    pygame.key.stop_text_input()
    save_tasks(tasks)
    pygame.quit()
    sys.exit()
