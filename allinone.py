from fastapi import FastAPI
from pydantic import BaseModel           

app = FastAPI()

class abc(BaseModel):
    name: str
    age: int
 
class xyz(BaseModel):
    a: int
    b: int

user_db = {
    1: {"name": "Alice", "age": 30},
    2: {"name": "Bob", "age": 25},  
}

@app.get("/addition")
def add(a:int, b:int):
    return a + b   

@app.post("/Multiply")
def multiply(data: xyz):
    return data.a * data.b

@app.put("/update_user/{user_id}")
def update_user(user_id: int, user: abc):
    if user_id in user_db:
        user_db[user_id] = user.dict()
        print(user_db)
        return {"message": "User updated  successfully"}
    else:
        return {"message": "User not found"}

@app.delete("/delete_user/{user_id}")
def delete_user(user_id: int):
    if user_id in user_db:
        del user_db[user_id]
        print(user_db)
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}   