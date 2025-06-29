import pygame

def main():
    # ─── 初期化 ───
    pygame.init()
    pygame.font.init()

    # ─── 定数 ───
    WIDTH, HEIGHT = 640, 480
    BG_COLOR      = (255, 255, 255)     # 白背景
    TEXT_COLOR    = (0,   0,   0)       # 黒文字
    INPUT_COLOR   = (0,   0, 128)       # 入力中の文字色（紺）
    RESULT_COLOR  = (128, 0,   0)       # 確定文字色（赤）
    BOX_COLOR     = (200, 200, 200)     # 入力欄の背景色
    MAX_LENGTH    = 20                  # 入力最大文字数

    # ─── 画面セットアップ ───
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Day4: 文字入力＆表示")
    clock  = pygame.time.Clock()

    # ─── フォント＆事前レンダリング ───
    font = pygame.font.Font(None, 48)
    instr_surf = font.render(
        "ここに入力してEnterを押そう:", True, TEXT_COLOR
    )

    # ─── 入力用変数 ───
    input_text = ""
    message    = ""

    running = True
    while running:
        # ─── イベント処理 ───
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    message    = input_text
                    input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    if len(input_text) < MAX_LENGTH:
                        input_text += event.unicode

        # ─── 描画 ───
        screen.fill(BG_COLOR)
        screen.blit(instr_surf, (20, 20))

        # 入力欄の枠
        box_rect = pygame.Rect(20, 80, WIDTH - 40, 50)
        pygame.draw.rect(screen, BOX_COLOR, box_rect)

        # 入力中の文字
        txt_surf = font.render(input_text, True, INPUT_COLOR)
        screen.blit(txt_surf, (box_rect.x + 5, box_rect.y + 5))

        # 確定した結果
        result_surf = font.render(f"結果: {message}", True, RESULT_COLOR)
        screen.blit(result_surf, (20, 160))

        pygame.display.flip()
        clock.tick(60)  # 60FPS

    pygame.quit()

if __name__ == "__main__":
    main()
