from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/dharmik/pansuriya")
def addd(a: int, b: int):
    return a + b

class subtractModel(BaseModel):
    a: int
    b: int


def sub(a: int, b:int):
    return a-b

@app.post("/")
def subractmodel(data: subtractModel):
    return sub(data.a,data.b)