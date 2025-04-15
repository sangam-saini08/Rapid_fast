from sqlmodel import Field,SQLModel
from sqlalchemy import Column, TIMESTAMP, text
from typing import Optional
from datetime import datetime


class Post(SQLModel,table = True):
    id : int = Field(default=None,primary_key=True)
    title:str = Field(default=None,nullable=False)
    content:str 
    published:bool = Field(default=False,nullable=False)
    created_at: Optional[datetime] = Field(
        sa_column=Column(
            TIMESTAMP(timezone=True),
            server_default=text("now()")
        )
    )
    # created_at = Column(TIMESTAMP(timezone=True),server_default=text('now()'))