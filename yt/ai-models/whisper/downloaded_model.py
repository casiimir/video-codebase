from transformers import pipeline
import os

os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_HUB_OFFLINE"] = "1"

LOCAL_MODEL_PATH = "models/whisper-large-v3-turbo"

pipe = pipeline(
  "automatic-speech-recognition",
  model=LOCAL_MODEL_PATH,
  device="cpu"
)

result = pipe("audio.wav", generate_kwargs={"language": "it", "task": "transcribe"})

print(result)