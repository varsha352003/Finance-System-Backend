from fastapi import FastAPI
import models
from database import engine, Base
from routes.users import router as user_router
from routes.transactions import router as transaction_router
from routes.summary import router as summary_router

app = FastAPI(
    title="Finance Tracking Backend",
    description="A finance management backend using FastAPI",
    version="1.0.0"
)

Base.metadata.create_all(bind=engine)

app.include_router(user_router)
app.include_router(transaction_router)
app.include_router(summary_router)

@app.get("/")
def home():
    return {"message": "Finance Tracking Backend is running"}
