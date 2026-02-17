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
    search_title=request.args.get('title')
    
    conn = sqlite3.connect('music_scenes.db')
    cursor = conn.cursor()
    
    #検索条件の組み立て
    query += 'SELECT * FROM scenes WHERE 1=1'
    params=[]
    
    if search_tag:
        query += ' AND tag LIKE ?'
        params.append('%' + search_tag + '%')

    if search_title:
        query += ' AND title LIKE ?'
        params.append('%' + search_title + '%')  

    cursor.execute(query, tuple(params))  
    
    scenes = []
    for row in cursor.fetchall():
        scenes.append({
            "id": row[0],
            "video_id": row[1],
            "title": row[2],
            "start_time": row[3],
            "tag": row[4],
            "description": row[5]
        })
    
    conn.close()
    return jsonify(scenes)
    

#スクリプトが直接実行された場合にサーバー起動
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)