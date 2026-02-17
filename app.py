from flask import Flask, jsonify, render_template, request
import sqlite3

#Flaskアプリケーションの初期化
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#ブラウザから/api/scenesにアクセスされたときの処理
@app.route('/api/scenes', methods=['GET'])
def get_scenes():
    # URLから '?tag=' の値を受け取る（指定がない場合は None）
    search_tag = request.args.get('tag')
    
    conn = sqlite3.connect('mv_scenes.db')
    cursor = conn.cursor()
    
    # タグが指定されている場合は絞り込み、指定がない場合は全て取得
    if search_tag:
        # 部分一致検索（例：「変身」で検索すると「変身シーン」もヒットする）
        cursor.execute("SELECT * FROM scenes WHERE tag LIKE ?", ('%' + search_tag + '%',))
    else:
        cursor.execute('SELECT * FROM scenes')
    
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
    return jsonify(scenes)
    

#スクリプトが直接実行された場合にサーバー起動
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)