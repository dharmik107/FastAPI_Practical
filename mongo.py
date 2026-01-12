from fastapi import FastAPI
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()
url = os.getenv("mongo_url")

client = AsyncIOMotorClient(url)
db = client["fastapi"]
data = db["fastapi_coll"]

app = FastAPI()

class coll(BaseModel):
    name:str
    age:int

@app.post("/insert/")
async def insert1(data1:coll):
   await data.insert_one(data1.dict())
   return {"Message":"Data Inserted"}

def del_id(doc):
    doc["id"] = str(doc["_id"])
    del doc["_id"]
    return doc


@app.get("/getdata/")
async def get_data():
    item = []
    data1 = data.find({})
    async   for i in data1:
        item.append(del_id(i))
    return item
