import sqlite3
from pathlib import Path

# נתיב לתיקיית database
BASE_DIR = Path(__file__).resolve().parent

def get_connection(db_name: str):
    """
    יוצר ומחזיר חיבור ל-SQLite
    db_name לדוגמה: 'users.db'
    """
    db_path = BASE_DIR / db_name
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row  # מאפשר גישה לפי שמות עמודות
    return conn
