from pydantic import BaseModel,ConfigDict


class UserIn(BaseModel):
    username:str
    email:str
    password:str


class Userout(BaseModel):
    id:int
    username:str
    email:str
    model_config = ConfigDict(from_attributes=True)
     