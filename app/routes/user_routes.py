from fastapi import APIRouter, Depends,HTTPException,status
from typing import Annotated
from sqlmodel import Session
from passlib.context import CryptContext
from ..database import get_session
from ..schemas.user_schema import UserIn,Userout
from ..models import user_model as models



router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.get("/{id}",response_model=Userout)
def get_user(id:int,db:Annotated[Session, Depends(get_session)]):
    first_user = db.query(models.User).filter(models.User.id == id).first()
    if not first_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return first_user

@router.get("/get_users",response_model=list[Userout])
def get_user(db:Annotated[Session, Depends(get_session)]):
    user = db.query(models.User).all()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return user

@router.post("/create_user")
async def create_user(payload:UserIn,db:Annotated[Session, Depends(get_session)]):
    hashed_pwd = pwd_context.hash(payload.password)
    user_data = payload.dict()
    user_data["password"] = hashed_pwd 


    # new_user = models.User(**payload.dict())
    new_user = models.User(**user_data)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message":"User created successfully", "user": new_user.username}