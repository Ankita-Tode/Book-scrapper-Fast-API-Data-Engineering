from fastapi import FastAPI
import sqlite3

app = FastAPI(title="Books API")
DB_FILE = "../db/books.db"

def get_books():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    rows = cursor.fetchall()
    conn.close()
    return [dict(row) for row in rows]

@app.get("/books")
def read_books():
    return get_books()