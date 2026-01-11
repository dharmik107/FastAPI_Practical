from fastapi import FastAPI
from pydantic import BaseModel  
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

db_url = 'postgresql://neondb_owner:npg_1WQIUvnG6XLZ@ep-blue-smoke-ahe5v4we-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'

class abc(BaseModel):
    name: str
    age: int

def connect_db():
    conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    return conn

def save_user(data):
    with open("user_data.txt", "a") as f:
        f.write(f"{data.name}, {data.age}\n")

@app.post("/create_user")
def create_user(user:abc):
    save_user(user)
    return {"message": "User created successfully"}

@app.post("/insert_user")
def insert_user(user:abc):
    connn = connect_db()
    cursor = connn.cursor()
    insert = "insert into user_table (name, age) values (%s, %s)"
    cursor.execute(insert, (user.name, user.age))
    connn.commit()
    cursor.close()
    connn.close()
    return {"message": "User inserted into database successfully"}
    