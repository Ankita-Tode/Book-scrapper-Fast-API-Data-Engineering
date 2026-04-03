# **B2B Book Data Pipeline**
Deployment link:https://book-scrapper-data-engineering--ankitamate.replit.app
# **🌟 Problem Statement**
Many businesses need up-to-date product data for analysis, pricing comparisons, or inventory tracking.  
This project demonstrates a **B2B-style data pipeline** that:

- Scrapes product data from an online bookstore  
- Cleans and standardizes the data  
- Stores it in a database  
- Exposes the data via an API for easy consumption  

**Source:** Books to Scrape (demo scraping site)

## 🏗️ Project Architecture

- Scraper (scraper.py)
- Data Cleaning (cleaning.py)
- Database (db.py)
- API (fastapi.py)
- Automation (Cron Job)


## 📁 Project Structure

```
project/
│
├── scraper/
│   └── scraper.py        # Scrapes data from website
│
├── pipeline/
│   ├── cleaning.py       # Data preprocessing and cleaning
│   └── pipeline.py       # Pipeline orchestration
│
├── database/
│   └── db.py             # Database connection & insertion
│
├── api/
│   └── fastapi.py        # API endpoints (/jobs)
│
├── logs/
│   └── pipeline.log      # Execution logs
│
├── requirements.txt      # Dependencies
└── README.md             # Documentation
```

# **🛠 Tech Stack**

- **Scraping:** Python, Requests, BeautifulSoup  
- **Data Cleaning:** Pandas, NumPy  
- **Database:** Sqlite 
- **API:** FastAPI, psycopg2  
- **Automation:** Cron Jobs  
- **Deployment:** Local machine, optionally Render / Railway / Replit  

# **⚡ Setup Instructions**

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd project

2. Create a virtual environment

python3 -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

3.Install dependencies

pip install -r requirements.txt


4.Environment Variables (optional but recommended)
Create a .env file in the root:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=
DB_NAME=clean_book
 
6 Run the pipeline manually
python pipeline/pipeline.py

🚀 API Usage

Start the FastAPI server:
uvicorn api.fastapi:app --reload

Access the data:
GET http://127.0.0.1:8000/jobs

⏰ Automation with Cron

Run the pipeline automatically every day at 2 AM:

Open the crontab editor:
crontab -e

Add the following entry:
0 2 * * * /usr/bin/python3 /path/to/project/pipeline/pipeline.py >> /path/to/project/logs/pipeline.log 2>&1
Adjust /usr/bin/python3 and paths according to your system
Logs are saved to pipeline.log

✅ Notes / Best Practices
Handle missing or inconsistent data carefully

Wrap API responses in JSON with column names for clarity
Keep credentials in .env rather than hardcoding
