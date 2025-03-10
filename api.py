"""
from fastapi import FastAPI
from pydantic import BaseModel
from language_detector import detect_language
from input_handler import preprocess_text

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/detect-language/")
async def detect_language_api(request: TextRequest):
    ''''''
    Detects language and preprocesses text.
    ''''''
    detected_data = detect_language(request.text)
    
    if detected_data["language"] in ["unknown", "unsupported"]:
        return detected_data  

    # Forward to input_handler for further processing
    processed_data = preprocess_text(detected_data["text"], detected_data["language"])
    
    return processed_data
"""
from fastapi import FastAPI
from pydantic import BaseModel
from language_detector import detect_language
from input_handler import preprocess_text

app = FastAPI()

class TextRequest(BaseModel):
    text: str

@app.post("/detect-language/")
async def detect_language_api(request: TextRequest):
    """
    Detects language and preprocesses text.
    """
    detected_data = detect_language(request.text)  # This is now a dictionary

    if detected_data["language"] in ["unknown", "unsupported"]:
        return {"error": "Language not supported or unknown"}

    # Pass the detected language to input_handler
    processed_data = preprocess_text(detected_data["text"], detected_data["language"])

    return processed_data

