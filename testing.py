from fastapi import FastAPI
from pydantic import BaseModel  

app = FastAPI() 

user_db = {
    1:{"name":"Dharmik", "age":21},
    2:{"name":"John", "age":25},
}