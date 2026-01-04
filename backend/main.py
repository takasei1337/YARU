from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from app.database import get_db
from fastapi import Depends



app = FastAPI(
    title="YARU API",
    description="Backend for YARU - Japanese Learning Platform",
    version="1.0.0"
)

# CORS configuration
origins = [
    "http://localhost:3000",  # Frontend Next.js
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to YARU API", "status": "running"}

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/health/db")
def health_check_db(db = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "database": "disconnected", "detail": str(e)}

