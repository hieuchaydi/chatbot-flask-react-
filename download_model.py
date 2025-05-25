# download_model.py
import gdown
import os

url = "https://drive.google.com/uc?id=1AbcDEfGhijKlmNOpqrStUVwxYZ"
output = "backend/trained_model/model.safetensors"

if not os.path.exists(output):
    print("Downloading model...")
    gdown.download(url, output, quiet=False)
else:
    print("Model already exists.")
