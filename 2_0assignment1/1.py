from fastapi import FastAPI, HTTPException, status
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI()

db_url = 'postgresql://neondb_owner:npg_1WQIUvnG6XLZ@ep-blue-smoke-ahe5v4we-pooler.c-3.us-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require'


def connect_db():
    return psycopg2.connect(db_url, cursor_factory=RealDictCursor)


@app.get("/student/{id}")
def get_student(id: int):
    conn = None
    cursor = None
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = "SELECT * FROM student WHERE id = %s"
        # pass parameters as a sequence (tuple/list)
        cursor.execute(query, (id,))
        student = cursor.fetchone()
        if student is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found")
        return student
    except psycopg2.Error as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    finally:
        if cursor:
            try:
                cursor.close()
            except Exception:
                pass
        if conn:
            try:
                conn.close()
            except Exception:
                pass