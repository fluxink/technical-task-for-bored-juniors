import sqlite3


class BoredDB:
    def __init__(self, db_name="bored.db"):
        self.db_name = db_name
        self.conn = None
        self.cursor = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS activities (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                activity TEXT,
                type TEXT,
                participants INTEGER,
                price REAL,
                link TEXT,
                key TEXT UNIQUE,
                accessibility REAL
            )
            """
        )
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.commit()
        self.conn.close()

    def save_activity(self, activity):
        self.cursor.execute(
            """
            INSERT OR IGNORE INTO activities
            (activity, type, participants, price, link, key, accessibility)
            VALUES (?, ?, ?, ?, ?, ?, ?)
            """,
            (
                activity["activity"],
                activity["type"],
                activity["participants"],
                activity["price"],
                activity["link"],
                activity["key"],
                activity["accessibility"],
            ),
        )
        self.conn.commit()

    def get_last_activities(self, n):
        self.cursor.execute(
            """
            SELECT * FROM activities ORDER BY id DESC LIMIT ?
            """,
            (n,),
        )
        return self.cursor.fetchall()
