from fastapi import Depends,Query,APIRouter
from sqlmodel import Session
from typing import Annotated
from ..database import get_session
from ..models import models
from ..schemas import schema


router = APIRouter()



@router.get('/get_posts')
def get_post(db: Annotated[Session, Depends(get_session)] ):
    posts = db.query(models.Post).all()
    print(posts)
    return posts

@router.post("/create_post")
def create_post(payload:schema.PostItem,db:Annotated[Session, Depends(get_session)]):
    new_post = models.Post(**payload.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post