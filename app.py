from flask import Flask, jsonify
import sqlite3

#Flaskアプリケーションの初期化
app = Flask(__name__)

#ブラウザから/api/scenesにアクセスされたときの処理
@app.route('/api/scenes', methods=['GET'])
def get_scenes():
    #データベースに接続
    conn = sqlite3.connect('music_scenes.db')
    cursor = conn.cursor()

    #データを全て取得
    cursor.execute('SELECT * FROM scenes')

    # 取得したデータをWebで扱いやすい形式（JSON）に変換
    scenes = []
    for row in cursor.fetchall():
        scenes.append({
            "id": row[0],
            "video_id": row[1],
            "start_time": row[2],
            "tag": row[3],
            "description": row[4]
        })
    
    conn.close()
    
    # データをブラウザに返す
    return jsonify(scenes)

#スクリプトが直接実行された場合にサーバー起動
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)