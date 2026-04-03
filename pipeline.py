import os
import pandas as pd
import sqlite3
from book_scraper import scrape_books  # Assuming you have a function to scrape books

# -----------------------------
# Paths
# -----------------------------
DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)  # create folder if missing
CSV_FILE = os.path.join(DATA_DIR, "books.csv")
DB_FILE = os.path.join(DATA_DIR, "books.db")

# -----------------------------
# Step 1: Ensure CSV exists
# -----------------------------
if not os.path.exists(CSV_FILE):
    print(f"{CSV_FILE} not found. Running scraper...")
    scrape_books()  # make sure your scraper saves to the same CSV_FILE

# -----------------------------
# Step 2: Clean data
# -----------------------------
def clean_data():
    df = pd.read_csv(CSV_FILE, encoding='utf-8-sig')

    # Clean price: remove any non-digit character
    df['Price'] = df['Price'].str.replace(r'[^\d.]', '', regex=True).astype(float)

    # Clean availability: extract number of books available
    df['availability'] = df['availability'].str.extract(r'(\d+)').fillna(0).astype(int)

    return df

# -----------------------------
# Step 3: Insert data into SQLite
# -----------------------------
def insert_into_sqlite(df):
    conn = sqlite3.connect(DB_FILE)
    df.to_sql("books", conn, if_exists="replace", index=False)
    conn.close()
    print(f"Data inserted into SQLite database at {DB_FILE}")

# -----------------------------
# Step 4: Run pipeline
# -----------------------------
def run_pipeline():
    df = clean_data()
    insert_into_sqlite(df)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()