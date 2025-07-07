#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import tkinter as tk
from tkinter import ttk
import sys

def fetch_headlines():
    """
    ニュースサイトから見出しとURLを取得してリストで返す。
    """
    url = "https://www3.nhk.or.jp/news/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }
    resp = requests.get(url, headers=headers)
    resp.encoding = resp.apparent_encoding   # 文字化け防止
    # ——— チェックポイント ———
    if resp.status_code != 200:
        raise RuntimeError(f"サイト取得失敗: ステータスコード {resp.status_code}")
    html = resp.text

    soup = BeautifulSoup(html, "html.parser")
    headlines = []
    seen = set()

    for a in soup.find_all("a"):
        text = a.get_text(strip=True)
        href = a.get("href", "")
        if text and href.startswith("/news/"):
            if text not in seen:
                seen.add(text)
                full_url = urljoin(url, href)
                headlines.append((text, full_url))

    return headlines

def build_gui(headlines):
    """
    Tkinterで見出しリストをスクロール表示するウィンドウを作成。
    """
    root = tk.Tk()
    root.title("最新ニュースヘッドライン")

    frame = ttk.Frame(root, padding=10)
    frame.pack(fill=tk.BOTH, expand=True)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    listbox = tk.Listbox(frame, yscrollcommand=scrollbar.set, width=80, height=25)
    for idx, (title, _) in enumerate(headlines, start=1):
        listbox.insert(tk.END, f"{idx}. {title}")
    listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar.config(command=listbox.yview)

    root.mainloop()

def main():
    try:
        hs = fetch_headlines()
    except Exception as e:
        print(f"【エラー】見出し取得中に例外発生: {e}", file=sys.stderr)
        sys.exit(1)

    if not hs:
        print("【警告】見出しが一件も取得できませんでした。", file=sys.stderr)
        sys.exit(1)

    build_gui(hs)

if __name__ == "__main__":
    main()
