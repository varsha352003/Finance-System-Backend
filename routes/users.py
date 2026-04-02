from fastapi import FastAPI
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import User
from schemas import UserCreate, UserResponse

router= APIRouter(prefix="/users",tags=["users"]) #Parameters set here apply to all routes registered on this router

@router.post("/",response_model=UserResponse) 
def create_user(user: UserCreate, db: Session=Depends(get_db)):
    new_user=User(
        name=user.name,
        email=user.email,
        role=user.role
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/",response_model=list[UserResponse])
def get_users(db:Session=Depends(get_db)): #This gets DB connection from database.py
    return db.query(User).all()
# this function queries the User table and returns all users. The response_model parameter ensures that the returned data is serialized according to the UserResponse schema, which converts SQLAlchemy objects into JSON responses.

@router.get("/{user_id}",response_model=UserResponse)
def get_user(user_id:int,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    return user

@router.patch("/{user_id}/role",response_model=UserResponse)
def update_role(user_id:int,role:str,db:Session=Depends(get_db)):
    user=db.query(User).filter(User.id==user_id).first()

    if not user:
        raise HTTPException(status_code=404,detail="User not found")
    user.role=role
    db.commit()
    db.refresh(user)

    return user
