from datetime import date
from pydantic import BaseModel

class UserCreate(BaseModel):
    name:str
    email:str
    role:str

class UserResponse(BaseModel):
    id:int
    name:str
    email:str
    role:str
    class Config:
        from_attributes=True

class TransactionCreate(BaseModel):
    amount:float
    type:str
    category:str
    date:date
    description:str | None=None
    user_id:int

class TransactionUpdate(BaseModel):
    amount:float | None=None
    type: str | None=None
    category:str | None=None
    date:date | None=None
    description:str | None=None

class TransactionResponse(BaseModel):
    id: int
    amount: float
    type: str
    category: str
    date: date
    description: str
    user_id: int

    class Config:
        from_attributes = True # Because DB will return SQLAlchemy object.This schema converts it into JSON response.

class SummaryResponse(BaseModel):
    total_income:float
    total_expense:float
    balance:float