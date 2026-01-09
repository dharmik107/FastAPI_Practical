from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class multiplymodel(BaseModel):
    a:int
    b:int

def domultiply(a:int, b:int):
    return a*b

@app.post("/multiply")
def mul(model: multiplymodel):
    return domultiply(model.a, model.b)