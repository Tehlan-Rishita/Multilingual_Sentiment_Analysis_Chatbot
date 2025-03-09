# api.py

from fastapi import FastAPI
from pydantic import BaseModel
import input_handler

app = FastAPI()

class TextInput(BaseModel):
    text: str

@app.post("/process")
async def process_text(input_data: TextInput):
    result = input_handler.preprocess_text(input_data.text)
    return result
