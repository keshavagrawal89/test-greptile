from fastapi import FastAPI
from db import insert_data, read_data

app = FastAPI()

@app.post("/insert")
def insert_endpoint(name: str, value: int):
    return insert_data(name, value)

@app.get("/read")
def read_endpoint():
    return read_data()

@app.get("/")
def index():
    return {"Hello": "World"}