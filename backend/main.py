from fastapi import FastAPI, UploadFile, File, Form
from typing import Dict
from botocore.exceptions import NoCredentialsError, BotoCoreError
import uuid
import os
import boto3

app = FastAPI()

# Read the secret code word from environment variable
SECRET_CODEWORD = os.getenv("SECRET_CODEWORD")
file_scan_results: Dict[str, bool] = {}

S3_BUCKET = "puzzlebox-user-uploads"
s3_client = boto3.client("s3")

# Completion word revealed only when the correct code word is guessed
COMPLETION_WORD = os.getenv("COMPLETION_WORD")

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    file_id = str(uuid.uuid4())
    key = f"uploads/{file_id}_{file.filename}"

    try:
        contents = await file.read()

        s3_client.put_object(
            Bucket=S3_BUCKET,
            Key=key,
            Body=contents,
            ContentType=file.content_type,
        )

        s3_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{key}"

        return {
            "message": "File uploaded to S3",
            "s3_key": key,
            "s3_url": s3_url
        }

    except (BotoCoreError, NoCredentialsError) as e:
        return {"error": f"Failed to upload to S3: {str(e)}"}

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
