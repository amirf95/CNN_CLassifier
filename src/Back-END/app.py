from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io
from testing import smart_predict
from pydantic import BaseModel
from Database import SessionLocal, Prediction

class SavePrediction(BaseModel):
    label: str
    confidence: float
    image_name: str
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model
model = load_model("C:\\Users\\amirf\\OneDrive\\Desktop\\Culex_Mosquito_Classifier\\models\\culex_binary_RGB_V4.keras")
CLASS_NAMES = ["Non-Culex", "Culex"]

def preprocess_image(image: Image.Image):
    image = image.resize((300, 300))
    image = img_to_array(image) / 255.0
    return np.expand_dims(image, axis=0)

@app.post("/predict")
async def predict(image: UploadFile = File(...)):

    if image.content_type not in ["image/jpeg", "image/png"]:
        raise HTTPException(400, "Only JPG or PNG images allowed")

    image_bytes = await image.read()
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    processed = preprocess_image(img)
    prediction = model.predict(processed)[0]

    idx = int(np.argmax(prediction))
    confidence = float(np.max(prediction))

    result = smart_predict(img)
    print(result)
    return {
        "label": result["label"],
        "probability": result["probability"],
        "confidence": result["confidence"]
    }

@app.post("/save")
def save_prediction(data: SavePrediction):
    db = SessionLocal()
    record = Prediction(
        label=data.label,
        confidence=data.confidence,
        image_name=data.image_name,
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    db.close()
    return {"status": "saved"}

@app.get("/history")
def get_history():
    db = SessionLocal()
    records = db.query(Prediction).order_by(Prediction.created_at.desc()).all()
    db.close()

    return [
        {
            "id": r.id,
            "label": r.label,
            "confidence": r.confidence,
            "image_name": r.image_name,
            "created_at": r.created_at.isoformat(),
        }
        for r in records
    ]
