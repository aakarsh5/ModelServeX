# app.py
import os, io
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
from PIL import Image
import numpy as np
import tensorflow as tf

layers = tf.keras.layers
models = tf.keras.models

app = FastAPI(title="CIFAR-10 TF FastAPI")

MODEL_PATH = os.environ.get('MODEL_PATH', 'model.h5')

labels = ['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
model = None

@app.on_event("startup")
def load_model():
    global model
    if not os.path.exists(MODEL_PATH):
        raise RuntimeError(f"Model not found at {MODEL_PATH}. Please train and save model first.")
    model = models.load_model(MODEL_PATH)

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert('RGB').resize((32, 32))
    arr = np.array(img).astype('float32') / 255.0
    arr = np.expand_dims(arr, 0)
    return arr

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Upload an image file.")
    contents = await file.read()
    try:
        x = preprocess_image(contents)
        preds = model.predict(x)
        top_idx = int(np.argmax(preds[0]))
        confidence = float(preds[0][top_idx])
        probs = {labels[i]: float(preds[0][i]) for i in range(len(labels))}
        return {"predicted_class": labels[top_idx], "class_index": top_idx, "confidence": confidence, "probabilities": probs}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {"message": "Welcome to the CIFAR-10 Image Classification API"}
