from flask import Flask, jsonify, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scenes', methods=['GET'])
def get_scenes():
    search_tag = request.args.get('tag')
    search_title = request.args.get('title')
    
    conn = sqlite3.connect('music_scenes.db')
    cursor = conn.cursor()
    
    # ベースとなるクエリを定義
    query = 'SELECT * FROM scenes WHERE 1=1'
    params = []
    
    # 検索条件があれば、クエリに追記していく（AND の前に半角スペースが必要です）
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

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)