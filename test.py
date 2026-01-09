from fastapi import FastAPI

app = FastAPI()

@app.get("/dharmik/pansuriya")
def addd(a: int, b: int):
    return a + b

@app.post("/")
def sub(a: int, b:int):
    return a-b