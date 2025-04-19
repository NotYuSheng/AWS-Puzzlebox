from fastapi import FastAPI, UploadFile, File, Form
from typing import Dict
import uuid
import os

app = FastAPI()

# Read the secret code word from environment variable
SECRET_CODEWORD = os.getenv("SECRET_CODEWORD")
file_scan_results: Dict[str, bool] = {}

# Completion word revealed only when the correct code word is guessed
COMPLETION_WORD = os.getenv("COMPLETION_WORD")

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    if not file.filename.endswith(".txt"): # or file.content_type != "text/plain":
        return {"error": "Only .txt files are allowed."}

    content = await file.read()
    text = content.decode("utf-8")
    
    found = SECRET_CODEWORD in text
    file_id = str(uuid.uuid4())
    file_scan_results[file_id] = found
    
    if found:
        message = f"Upload successful. 🎉 The code word was found in {file.filename}!"
    else:
        message = f"Upload successful. The code word was NOT found in {file.filename}. Try again!"

    return {
        "message": message,
        "file_id": file_id
    }

@app.post("/guess")
async def guess_codeword(codeword: str = Form(...)):
    # Basic input validation to prevent injection attacks
    if not codeword or not isinstance(codeword, str):
        return {"result": "Invalid code word. Try again."}

    if codeword.strip().lower() == SECRET_CODEWORD.lower():
        return {
            "result": "Correct! Well done, you completed the puzzle-box! Save the completion_word as proof of completion.",
            "completion_word": COMPLETION_WORD
        }
    return {
        "result": "Incorrect code word. Try again."
    }
