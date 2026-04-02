from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Transaction
from schemas import SummaryResponse, TransactionResponse
from services.analytics import (
    calculate_income,
    calculate_expense,
    calculate_balance,
    category_breakdown,
    monthly_summary,
    recent_activity
)

router = APIRouter(prefix="/summary", tags=["Summary"])


@router.get("/", response_model=SummaryResponse)
def get_summary(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()

    return SummaryResponse(
        total_income=calculate_income(transactions),
        total_expense=calculate_expense(transactions),
        balance=calculate_balance(transactions)
    )

@router.get("/category")
def get_category_summary(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return category_breakdown(transactions)

@router.get("/monthly")
def get_monthly_summary(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return monthly_summary(transactions)

@router.get("/recent", response_model=list[TransactionResponse])
def get_recent_activity(db: Session = Depends(get_db)):
    transactions = db.query(Transaction).all()
    return recent_activity(transactions)