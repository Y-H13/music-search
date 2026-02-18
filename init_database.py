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
('YJRFD1SAd-8', '櫻坂46', 'Start over!', '覚悟', '圧倒的な表現力と、何度も立ち上がる力強さを感じる一曲'),
    ('x_Zsyu2K5G4', '櫻坂46', '承認欲求', '葛藤', '現代のSNS社会における若者のリアルな心情を描いた作品'),
    ('7R3U7d7dEWE', '櫻坂46', '何歳の頃に戻りたいのか？', '前向き', '過去を振り返りつつも、未来へ進む決意を歌ったエモーショナルな楽曲')
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
