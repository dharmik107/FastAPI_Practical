from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

db_url = 'postgresql://neondb_owner:npg_1WQIUvnG6XLZ@ep-blue-smoke-ahe5v4we-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'  

def connect_db():
    conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
    return conn

@app.get("/student")
def get_student(id:int):
    conn = connect_db()
    cursor = conn.cursor()
    query = "SELECT * FROM student_table where id=%s"
    cursor.execute(query, id)   
    student = cursor.fetchone()
    cursor.close()  
    conn.close()
    return student