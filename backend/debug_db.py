import psycopg2
import os
from dotenv import load_dotenv
import urllib.parse

load_dotenv()

url = os.getenv("DATABASE_URL")
print(f"Testing URL: {url.split('@')[-1]}") # Print host only

try:
    conn = psycopg2.connect(url)
    print("Connection SUCCESS")
    conn.close()
except Exception as e:
    print(f"Connection FAILED: {e}")
