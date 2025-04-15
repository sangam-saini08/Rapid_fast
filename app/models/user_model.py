from sqlmodel import Field,SQLModel
from sqlalchemy import Column, TIMESTAMP, text
from typing import Optional
from datetime import datetime


class User(SQLModel,table = True):
    id : int = Field(default=None,primary_key=True)
    username:str = Field(default=None,nullable=False)
    email:str = (Field(default=None,nullable=False,unique=True))
    password:str = Field(default=None,nullable=False)
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            server_default=text("now()")
        )
    )
   