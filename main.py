from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class User(BaseModel):
    name:str
@app.get("/")
async def hello_world():
    return {"message":"Hello World"}


@app.get("/hello/{name}")
async def hello_name(name:str):
    return {"message":f"Hello {name}"}


@app.post("/hello-post")
async def hello_name(user:User):
    return {"message":f"Hello {user.name}"}