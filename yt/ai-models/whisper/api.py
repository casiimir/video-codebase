import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

app = FastAPI()

class TranscriptionRequest(BaseModel):
    audio_file: str

LOCAL_MODEL_PATH = "models/whisper-large-v3-turbo"

pipe = pipeline("automatic-speech-recognition", model=LOCAL_MODEL_PATH, device="cpu")

@app.get("/")
async def root():
    return {"message": "Welcome to the Whisper ASR API!"}

@app.post("/transcribe")
async def transcribe_audio(request: TranscriptionRequest):
    audio_path = request.audio_file

    result = pipe(audio_path, generate_kwargs={"language": "it", "task": "transcribe"})

    text = result["text"]

    return {"transcription": text}