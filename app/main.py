from fastapi import FastAPI
from .database import create_db_and_tables
from .routes import post_routes,user_routes

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.include_router(user_routes.router, prefix="/api/v1/users", tags=["users"])
app.include_router(post_routes.router, prefix="/api/v1/posts", tags=["posts"])    

@app.get("/")
def read_root():
    return {"Hello": "World from FastAPI!"}


    
