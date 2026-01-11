from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, validator
from typing import List
import json
from pathlib import Path

app = FastAPI()


class Course(BaseModel):
    id: int 
    name: str 
    credits: int 
    instructor: str 


@app.post("/save_data")
def savedata(courses: List[Course]):
    file_path = Path("courses.json")
    existing = []

    if file_path.exists():  

        with file_path.open("r", encoding="utf-8") as f:
            existing = json.load(f)

            if not isinstance(existing, list):
                existing = []

        new_records = [c.dict() for c in courses]
        
        existing.extend(new_records)

        with file_path.open("w", encoding="utf-8") as f:
            json.dump(existing, f, ensure_ascii=False, indent=2)

        return {"message": "Data saved successfully", "count": len(new_records)}
   