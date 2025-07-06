# 必要なライブラリを読み込む（道具を準備する）
import requests
import json

# 呼び出したいAPIの住所（URL）
# 今回はJSONPlaceholderのユーザー情報を取得するAPI
url = "https://jsonplaceholder.typicode.com/users"

print("APIからデータを取得します...")

# APIを呼び出す処理（エラーが起きる可能性のある処理）
try:
    # requests.get() で、指定したURLに情報をリクエストする（ウェイターに注文する）
    response = requests.get(url)

    # ステータスコードのチェック
    # 200番台でなければエラーを発生させる (例: 404 Not Found, 500 Server Error)
    response.raise_for_status()

    # 取得したデータをJSON形式からPythonが扱える形式（リストや辞書）に変換する
    users_data = response.json()

    print("データの取得に成功しました！")
    print("---")

    # 取得したデータの中から、最初の3人分の情報だけ表示してみる
    print("ユーザー情報（先頭3名）:")
    for user in users_data[:3]:
        print(f"  名前: {user['name']}")
        print(f"  ユーザー名: {user['username']}")
        print(f"  Email: {user['email']}")
        print(f"  ウェブサイト: {user['website']}")
        print("  ---")

# API呼び出し中にエラーが起きた場合の処理
except requests.exceptions.RequestException as e:
    print(f"エラーが発生しました: 通信に問題があるかもしれません。")
    print(f"エラー詳細: {e}")

# JSONの変換中にエラーが起きた場合の処理
except json.JSONDecodeError:
    print("エラーが発生しました: サーバーから正しいJSONデータが返されませんでした。")