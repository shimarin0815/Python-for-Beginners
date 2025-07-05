import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

class ImageViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("シンプル画像ビューワー")
        self.canvas = tk.Canvas(root, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)

        # ボタン用フレーム
        frame = tk.Frame(root)
        frame.pack(fill=tk.X)
        tk.Button(frame, text="画像選択", command=self.select_images).pack(side=tk.LEFT)
        tk.Button(frame, text="← 前へ",   command=self.prev_image).pack(side=tk.LEFT)
        tk.Button(frame, text="次へ →", command=self.next_image).pack(side=tk.LEFT)

        self.images = []
        self.index = 0

    def select_images(self):
        # 複数ファイル選択ダイアログ（TIFF まで対応）
        files = filedialog.askopenfilenames(
            title="表示したい画像を選択",
            filetypes=[("画像ファイル", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.tif;*.tiff")]
        )
        print("✔ 選択された画像ファイル:", files)  # デバッグ出力
        if not files:
            return
        self.images = list(files)
        self.index = 0
        self.show_image()

    def show_image(self):
        if not self.images:
            return
        path = self.images[self.index]
        try:
            img = Image.open(path)
        except Exception as e:
            messagebox.showerror("画像オープンエラー",
                                 f"{os.path.basename(path)} を開けませんでした。\n{e}")
            return

        # ── ウィンドウ／キャンバスサイズを最新化 ──
        self.root.update_idletasks()
        canvas_w = self.canvas.winfo_width()
        canvas_h = self.canvas.winfo_height()
        print(f"✔ canvas size: {canvas_w}×{canvas_h}, original image size: {img.size}")
        # ────────────────────────────────────────

        # リサイズ（縦横比を保ったままキャンバス内に収める）
        img = img.copy()
        img.thumbnail((canvas_w, canvas_h), Image.LANCZOS)

        self.photo = ImageTk.PhotoImage(img)
        self.canvas.delete("all")
        self.canvas.create_image(canvas_w//2, canvas_h//2,
                                 image=self.photo, anchor=tk.CENTER)
        self.root.title(
            f"画像ビューワー — {os.path.basename(path)} ({self.index+1}/{len(self.images)})"
        )

    def prev_image(self):
        if self.index > 0:
            self.index -= 1
            self.show_image()

    def next_image(self):
        if self.index < len(self.images) - 1:
            self.index += 1
            self.show_image()

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(400, 300)
    app = ImageViewer(root)
    root.mainloop()

