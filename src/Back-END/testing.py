import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

MODEL_PATH = r"C:\Users\amirf\OneDrive\Desktop\Culex_Mosquito_Classifier\models\culex_binary_RGB_V4.keras"
IMAGE_SIZE = (300, 300)

THRESHOLD = 0.7
UNCERTAIN_LOW = 0.35
UNCERTAIN_HIGH = 0.65

model = load_model(MODEL_PATH)
print("✅ Model loaded")

def predict_from_pil(pil_img):
    img = pil_img.resize(IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)

    prob = float(model.predict(img_array)[0][0])
    return prob

def smart_predict(pil_img):
    probs = []
    prob = predict_from_pil(pil_img)
    probs.append(prob)

    # Rotation logic if uncertain
    if UNCERTAIN_LOW <= prob <= UNCERTAIN_HIGH:
        img_rot = pil_img.copy()
        for _ in range(3):
            img_rot = img_rot.rotate(90, expand=True)
            probs.append(predict_from_pil(img_rot))

    avg_prob = float(np.mean(probs))

    if avg_prob >= THRESHOLD:
        return {
            "label": "non-culex",
            "probability": avg_prob,
            "confidence": avg_prob
        }
    elif avg_prob <= (1 - THRESHOLD):
        return {
            "label": "culex",
            "probability": avg_prob,
            "confidence": 1 - avg_prob
        }
    else:
        return {
            "label": "uncertain",
            "probability": avg_prob,
            "confidence": 1 - abs(avg_prob - 0.5) * 2
        }
print("✅ Prediction function ready")
