from fastapi import FastAPI
from pydantic import BaseModel  

app = FastAPI() 

user_db = {
    1:{"name":"Dharmik", "age":21},
    2:{"name":"Skano", "age":25},
    3:{"name":"John", "age":30}
}

class User(BaseModel):
    name: str
    age: int

@app.put("/user/update/{id}")
def user_update(id: int, user:User):
    if id in user_db:
        user_db[id] = user.dict()
        print(user_db)  
        return {"message": "User updated successfully", "user": user_db[id]}
    else:
        return {"error": "User not found"}


@app.delete("/user/delete/{id}")
def delete_user(id:int):
    if id in user_db:
        del user_db[id]
        print(user_db)
        return {"Message":"User deleted successfully"}
    else:
        return {"Error":"User not found"}

