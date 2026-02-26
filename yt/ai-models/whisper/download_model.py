from huggingface_hub import snapshot_download

MODEL_ID = "openai/whisper-large-v3-turbo"
LOCAL_DIR = "./models/whisper-large-v3-turbo"

snapshot_download(repo_id=MODEL_ID, local_dir=LOCAL_DIR, local_dir_use_symlinks=False)

print(f"Model '{MODEL_ID}' has been downloaded to '{LOCAL_DIR}'.")