from app.database import SessionLocal
from sqlalchemy import text
import os
import traceback

def test_connection():
    try:
        db = SessionLocal()
        result = db.execute(text("SELECT 1"))
        print("Database connection successful:", result.scalar())
    except Exception:
        with open("error.log", "w") as f:
            f.write(traceback.format_exc())
        print("Error logged to error.log")
    finally:
        db.close()

if __name__ == "__main__":
    test_connection()
