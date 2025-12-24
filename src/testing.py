import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

# ===== CONFIG =====
MODEL_PATH = r"C:\Users\amirf\OneDrive\Desktop\Culex_Mosquito_Classifier\models\culex_binary_RGB_V3.keras"
#IMAGE_SIZE = (224, 224)
IMAGE_SIZE = (300, 300)  # for B3
THRESHOLD = 0.7   # decision boundary

UNCERTAIN_LOW = 0.35
UNCERTAIN_HIGH = 0.65
# ===== LOAD MODEL ONCE =====
model = load_model(MODEL_PATH)
print("✅ Model loaded")

# ===== HELPER FUNCTION TO PREDICT FROM PIL IMAGE =====
from tensorflow.keras.applications.efficientnet import preprocess_input

def predict_from_pil(pil_img):
    img_array = image.img_to_array(pil_img)
    img_array = preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0)
    prob = model.predict(img_array)[0][0]
    return prob

# ===== FUNCTION TO PREDICT ONE IMAGE =====
def predict_image(img_path):
    if not os.path.exists(img_path):
        print("❌ Image not found")
        return

    # Load and preprocess image
    img = image.load_img(img_path, target_size=IMAGE_SIZE)
    img_array = image.img_to_array(img)
    img_array = preprocess_input(img_array) 
    img_array = np.expand_dims(img_array, axis=0)  # (1, 300, 300, 3)

    # Prediction
    prob = model.predict(img_array)[0][0]

    if prob >= THRESHOLD:
        label = "non_culex"
        confidence = prob
    else:
        label = "culex"
        confidence = 1 - prob
    
    probs=[prob]  # containig all probabilities for analysis

    if UNCERTAIN_LOW <= prob <= UNCERTAIN_HIGH:
        print(f"Original prob: {prob:.3f}")
        print("⚠️ Uncertain prediction → trying rotations")

        img_rot = img.copy()

        for _ in range(3):  # 90°, 180°, 270°
            img_rot = img_rot.rotate(90, expand=True)
            prob_rot = predict_from_pil(img_rot)
            probs.append(prob_rot)


            print(f"🔄 Rotated prob: {prob_rot:.3f}")
            best_prob = np.mean(probs)
            if best_prob >= 0.65:
                label = "culex"
                confidence = best_prob
            elif best_prob <= 0.35:
                label = "non_culex"
                confidence = 1 - best_prob
            else:
                label = "UNCERTAIN"
                confidence = 1 - abs(best_prob - 0.5) * 2
            print(f"⭐ Best prob so far: {best_prob:.3f}")
    print(f"🦟 Prediction: {label.upper()}")
    print(f"📊 Confidence: {confidence:.2%}")

# ===== INTERACTIVE LOOP =====
while True:
    img_path = input("Enter image path (or 'q' to quit): ").strip()
    
    if img_path.lower() == 'q':
        print("👋 Exiting")
        break

    predict_image(img_path)
    
