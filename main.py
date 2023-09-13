from fastapi import FastAPI

app=FastAPI()

@app.get("/")
async def hello_world():
    return {"message":"Hello World"}


@app.get("/hello/{name}")
async def hello_name(name:str):
    return {"message":f"Hello {name}"}