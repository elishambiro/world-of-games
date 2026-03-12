import sqlite3
import os
import requests

DB_PATH = os.environ.get('DB_PATH', 'data/scores.db')


def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            name TEXT PRIMARY KEY,
            score INTEGER NOT NULL DEFAULT 0
        )
    ''')
    conn.commit()
    _migrate_from_txt(conn)
    conn.close()


def _migrate_from_txt(conn):
    txt_path = 'templates/scores.txt'
    if not os.path.exists(txt_path):
        return
    count = conn.execute('SELECT COUNT(*) FROM scores').fetchone()[0]
    if count > 0:
        return
    with open(txt_path, 'r') as f:
        for line in f:
            parts = line.split()
            if len(parts) == 2:
                conn.execute(
                    'INSERT OR IGNORE INTO scores (name, score) VALUES (?, ?)',
                    (parts[0], int(parts[1]))
                )
    conn.commit()


def points_of_winning(difficulty):
    return (difficulty * 3) + 5


def record_play(game, difficulty, result):
    try:
        requests.post(
            'http://localhost:5000/api/record_play',
            json={"game": game, "difficulty": difficulty, "result": result},
            timeout=1
        )
    except Exception:
        pass


def add_score(name, points):
    init_db()
    conn = sqlite3.connect(DB_PATH)
    conn.execute(
        'INSERT INTO scores (name, score) VALUES (?, ?) '
        'ON CONFLICT(name) DO UPDATE SET score = score + ?',
        (name, points, points)
    )
    conn.commit()
    conn.close()


def get_all_scores():
    init_db()
    conn = sqlite3.connect(DB_PATH)
    rows = conn.execute('SELECT name, score FROM scores ORDER BY score DESC').fetchall()
    conn.close()
    return [{"name": row[0], "score": row[1]} for row in rows]
