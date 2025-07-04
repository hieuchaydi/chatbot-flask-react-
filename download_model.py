# download_model.py
import gdown
import os

url = "https://drive.google.com/drive/u/0/folders/1Uz06kBuGJ3ZEl1lQPuTPv-D3erl4flu2"
output = "backend/trained_model/model.safetensors"

if not os.path.exists(output):
    print("Downloading model...")
    gdown.download(url, output, quiet=False)
else:
    print("Model already exists.")
