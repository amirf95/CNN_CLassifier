import os
import shutil
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.efficientnet import preprocess_input

# ===== PATHS (EDIT ONLY THESE IF NEEDED) =====
MODEL_PATH = r"C:\Users\amirf\OneDrive\Desktop\Culex_Mosquito_Classifier\models\culex_binary_RGB_V4.keras"
DATASET_DIR = r"C:\Users\amirf\Downloads\dataset"
OUTPUT_DIR = "wrong_predictions_val"

IMG_SIZE = (300, 300)
BATCH_SIZE = 1
THRESHOLD = 0.5

# ===== CREATE OUTPUT DIRS =====
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "non_culex_as_culex"), exist_ok=True)
os.makedirs(os.path.join(OUTPUT_DIR, "culex_as_non_culex"), exist_ok=True)

# ===== LOAD MODEL =====
model = tf.keras.models.load_model(MODEL_PATH)

# ===== LOAD VALIDATION DATA (NO SHUFFLE!) =====
val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    validation_split=0.15
)

val_dataset = val_datagen.flow_from_directory(
    DATASET_DIR,
    target_size=IMG_SIZE,
    color_mode="rgb",
    batch_size=BATCH_SIZE,
    class_mode="binary",
    subset="validation",
    shuffle=False
)

# ===== PREDICT =====
val_dataset.reset()
pred_probs = model.predict(val_dataset, verbose=1)
pred_labels = (pred_probs > THRESHOLD).astype(int).flatten()

true_labels = val_dataset.classes
filenames = val_dataset.filenames

# ===== EXTRACT WRONG PREDICTIONS =====
for i in range(len(true_labels)):
    true = true_labels[i]
    pred = pred_labels[i]
    confidence = float(pred_probs[i])

    if true != pred:
        src_path = os.path.join(DATASET_DIR, filenames[i])

        if true == 0 and pred == 1:
            dst = os.path.join(OUTPUT_DIR, "non_culex_as_culex")
        else:
            dst = os.path.join(OUTPUT_DIR, "culex_as_non_culex")

        filename = os.path.basename(filenames[i])
        new_name = f"{confidence:.2f}_{filename}"

        shutil.copy(src_path, os.path.join(dst, new_name))

print("✅ Wrong validation images extracted successfully!")
