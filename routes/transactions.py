from fastapi import APIRouter, Depends , HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Transaction
from schemas import TransactionCreate, TransactionResponse, TransactionUpdate

router=APIRouter(prefix="/transactions",tags=["transactions"]) 

# so all apis automatically start with /transactions

@router.post("/",response_model=TransactionResponse)
def create_transaction(transaction: TransactionCreate, db: Session=Depends(get_db)):
    new_transaction=Transaction(**transaction.dict())
    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return new_transaction

@router.get("/",response_model=list[TransactionResponse])
def get_transactions(db:Session=Depends(get_db)):
    return db.query(Transaction).all()

@router.get("/{transaction_id}",response_model=TransactionResponse)
def get_transaction(transaction_id:int,db:Session=Depends(get_db)):
    transaction=db.query(Transaction).filter(Transaction.id==transaction_id).first()

    if not transaction:
        raise HTTPException(status_code=404,detail="Transaction not found")
    return transaction

@router.put("/{transaction_id}",response_model=TransactionResponse)
def update_transaction(transaction_id:int,updated_data:TransactionUpdate,db: Session=Depends(get_db)):
    transaction=db.query(Transaction).filter(Transaction.id==transaction_id).first()

    if not transaction:
        raise HTTPException(status_code=404,detail="Transaction not found")
    
    for key,value in updated_data.dict(exclude_unset=True).items():
        setattr(transaction,key,value)
    db.commit()
    db.refresh(transaction)

    return transaction

@router.delete("/{transaction_id}")
def delete_transaction(transaction_id: int, db: Session = Depends(get_db)):
    transaction = db.query(Transaction).filter(Transaction.id == transaction_id).first()

    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")

    db.delete(transaction)
    db.commit()

    return {"message": "Transaction deleted successfully"}

@router.get("/filter", response_model=list[TransactionResponse])
def filter_transactions(category: str = None, type: str = None, db: Session = Depends(get_db)):
    query = db.query(Transaction)

    if category:
        query = query.filter(Transaction.category == category)

    if type:
        query = query.filter(Transaction.type == type)

    return query.all()