import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_books():
    # -----------------------------
    # Create 'data' folder if it doesn't exist
    # -----------------------------
    os.makedirs("data", exist_ok=True)  # folder will be created in project directory

    # -----------------------------
    # Scraper setup
    # -----------------------------
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"  # Example URL
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to load page: {url}")

    soup = BeautifulSoup(response.text, "html.parser")

    # -----------------------------
    # Extract book data
    # -----------------------------
    books = []
    for book in soup.select("article.product_pod"):
        title = book.h3.a["title"]
        price = book.select_one("p.price_color").text
        availability = book.select_one("p.availability").text.strip()
        books.append({"Title": title, "Price": price, "availability": availability})

    # -----------------------------
    # Convert to DataFrame
    # -----------------------------
    df = pd.DataFrame(books)

    # -----------------------------
    # Save CSV safely
    # -----------------------------
    csv_path = os.path.join("data", "books.csv")
    df.to_csv(csv_path, index=False)
    print(f"CSV saved successfully at {csv_path}")

# -----------------------------
# Optional: allow running this file directly
# -----------------------------
if __name__ == "__main__":
    scrape_books()
