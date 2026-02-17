import sqlite3

#1 データベースに接続
conn=sqlite3.connect('music_scenes.db')
cursor = conn.cursor()

#2 テーブルの作成
cursor.execute('''
CREATE TABLE IF NOT EXISTS scenes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    video_id TEXT NOT NULL,
    title TEXT NOT NULL,
    start_time TNTEGER NOT NULL,
    tag TEXT NOT NULL,
    description TEXT
)
''')

# 3. サンプルデータの準備
# 実際のYouTube ID（例：dQw4w9WgXcQ）に置き換えて使用します
sample_data = [
    ('video_id_A', 'Awesome Song', 65, '変身シーン', '主人公が覚悟を決めてフォームチェンジする熱いシーン'),
    ('video_id_B', 'Dance Anthem', 120, '圧倒的なダンス', 'サビ前のフォーメーション移動とセンターの表情が最高'),
    ('video_id_A', 'Awesome Song', 185, '切ない', '雨の中での印象的な横顔')
]

# 4. データを一括で挿入
cursor.executemany('''
INSERT INTO scenes (video_id, title, start_time, tag, description)
VALUES (?, ?, ?, ?, ?)
''', sample_data)

# 5. 変更を確定（保存）
conn.commit()

# 6. 登録したデータを検索して表示（動作確認）
print("--- 登録されたシーン一覧 ---")
cursor.execute('SELECT * FROM scenes')
for row in cursor.fetchall():
    print(f"ID: {row[0]}, 曲名: {row[1]}, Video: {row[2]}, {row[3]}秒, タグ: {row[4]}, メモ: {row[4]}")

# 7. 接続を閉じる
conn.close()
