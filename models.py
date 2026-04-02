from database import Base
from sqlalchemy import Column, Integer,String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    email=Column(String,unique=True,nullable=False)
    role=Column(String,nullable=False,default="viewer")
    transactions = relationship("Transaction", back_populates="user")


class Transaction(Base):
    __tablename__="transactions"

    id=Column(Integer,primary_key=True,index=True)
    amount=Column(Float,nullable=False)
    type=Column(String,nullable=False)
    category=Column(String,nullable=False)
    date=Column(Date,nullable=False)
    description=Column(String)
    user_id=Column(Integer,ForeignKey("users.id"),nullable=False)
    user = relationship("User", back_populates="transactions")