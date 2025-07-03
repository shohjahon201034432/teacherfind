import sqlite3

def init_db():
    conn = sqlite3.connect("ustoz.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS teachers (
            id INTEGER PRIMARY KEY,
            user_id INTEGER,
            fullname TEXT,
            subject TEXT,
            description TEXT,
            telegram TEXT,
            phone TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_teacher(user_id, fullname, subject, description, telegram, phone):
    conn = sqlite3.connect("ustoz.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO teachers (user_id, fullname, subject, description, telegram, phone) VALUES (?, ?, ?, ?, ?, ?)",
                (user_id, fullname, subject, description, telegram, phone))
    conn.commit()
    conn.close()

def get_teachers_by_subject(subject):
    conn = sqlite3.connect("ustoz.db")
    cur = conn.cursor()
    cur.execute("SELECT fullname, description, telegram, phone FROM teachers WHERE subject=?", (subject,))
    result = cur.fetchall()
    conn.close()
    return result
