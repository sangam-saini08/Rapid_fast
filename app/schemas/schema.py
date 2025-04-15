from pydantic import BaseModel,ConfigDict


class Item(BaseModel):
    title:str
    content:str
    published:bool = True


class PostItem(Item):
    pass

# class PostResponse(Item):
#     pass
#     model_config = ConfigDict(from_attributes=True)
       