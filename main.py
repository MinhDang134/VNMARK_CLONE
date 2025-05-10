import uvicorn
from fastapi import FastAPI, Depends
from sqlmodel import Session, select
from typing import List
from src.posts.router import router
from database import get_db
import logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()

# Thêm prefix cho router
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8005, reload=True)
