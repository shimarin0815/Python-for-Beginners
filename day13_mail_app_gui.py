import tkinter as tk
from tkinter import messagebox  # ポップアップメッセージ用にインポート
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# --- Step2: メール送信機能 ---
def send_email():
    # 入力欄から情報を取得する
    to_address = entry_to.get()
    subject = entry_subject.get()
    body = text_body.get("1.0", tk.END) # Textウィジェットからの取得方法

    # ★★★ 自分の情報に書き換える ★★★
    my_address = "shimada.kouta@gmail.com"
    app_password = "vtew ixlk idaj yrtg"
    # ★★★★★★★★★★★★★★★★★★★★

    # 宛先が入力されていなかったらエラーメッセージを出す
    if not to_address:
        messagebox.showerror("エラー", "宛先を入力してください。")
        return # 処理を中断

    # メールの設定
    try:
        # 日本語を扱うための設定
        msg = MIMEText(body, 'plain', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = my_address
        msg['To'] = to_address

        # Gmailのサーバーに接続してメールを送信
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_address, app_password)
        server.send_message(msg)
        server.quit()

        # 送信完了のメッセージをポップアップで表示
        messagebox.showinfo("成功", "メールが正常に送信されました！")

    except Exception as e:
        # エラーが起きたらメッセージを表示
        messagebox.showerror("送信エラー", f"エラーが発生しました:\n{e}")

# --- Step1: 画面の作成 ---
window = tk.Tk()
window.title("メール送信アプリ")
window.geometry("500x450") # ウィンドウのサイズを指定

# --- 部品の作成と配置 ---
# 宛先ラベルと入力ボックス
label_to = tk.Label(window, text="宛先 (To):")
label_to.pack(pady=5)
entry_to = tk.Entry(window, width=50)
entry_to.pack(pady=5)

# 件名ラベルと入力ボックス
label_subject = tk.Label(window, text="件名 (Subject):")
label_subject.pack(pady=5)
entry_subject = tk.Entry(window, width=50)
entry_subject.pack(pady=5)

# 本文ラベルと入力ボックス
label_body = tk.Label(window, text="本文 (Body):")
label_body.pack(pady=5)
text_body = tk.Text(window, width=50, height=15)
text_body.pack(pady=5)

# 送信ボタン (押されたら send_email 関数を呼び出すように command を設定)
button_send = tk.Button(window, text="送信", command=send_email)
button_send.pack(pady=20)

# --- ウィンドウの表示 ---
window.mainloop()