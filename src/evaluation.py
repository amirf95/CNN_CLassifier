from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix, classification_report
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import roc_curve, auc, precision_recall_curve

# ===== Paths =====
VAL_DIR = r"C:\Users\amirf\OneDrive\Desktop\Culex_Mosquito_Classifier\data\Val"  # adjust if needed
MODEL_PATH = r"C:\Users\amirf\OneDrive\Desktop\Culex_Mosquito_Classifier\models\culex_binary_RGB.keras"

# ===== Data generator (MUST MATCH TRAINING) =====
from tensorflow.keras.applications.efficientnet import preprocess_input

val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

val_dataset = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    shuffle=False
)

# ===== Load model =====
model = load_model(MODEL_PATH)

# ===== Evaluation =====
val_dataset.reset()

y_true = val_dataset.classes
y_pred_probs = model.predict(val_dataset)
y_pred = (y_pred_probs > 0.5).astype(int).reshape(-1)

cm = confusion_matrix(y_true, y_pred)
print("Confusion Matrix:\n", cm)

print("\nClassification Report:\n")
print(classification_report(
    y_true,
    y_pred,
    target_names=["non_culex", "culex"]
))
plt.figure(figsize=(5,5))
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.colorbar()

classes = ["non_culex", "culex"]
tick_marks = np.arange(len(classes))
plt.xticks(tick_marks, classes)
plt.yticks(tick_marks, classes)

for i in range(2):
    for j in range(2):
        plt.text(j, i, cm[i, j],
                 ha="center", va="center")

plt.ylabel("True label")
plt.xlabel("Predicted label")
plt.tight_layout()
plt.show()
# ===== ROC Curve =====
fpr, tpr, _ = roc_curve(y_true, y_pred_probs)
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, label=f"AUC = {roc_auc:.3f}")
plt.plot([0,1], [0,1], linestyle="--")
plt.xlabel("False Positive Rate")
plt.ylabel("True Positive Rate")
plt.title("ROC Curve")
plt.legend()
plt.grid()
plt.show()
# ===== Precision-Recall Curve =====
precision, recall, _ = precision_recall_curve(y_true, y_pred_probs)

plt.figure()
plt.plot(recall, precision)
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision–Recall Curve")
plt.grid()
plt.show()

plt.figure()
plt.hist(y_pred_probs[y_true == 0], bins=30, alpha=0.6, label="non_culex")
plt.hist(y_pred_probs[y_true == 1], bins=30, alpha=0.6, label="culex")
plt.axvline(0.5, linestyle="--")
plt.xlabel("Predicted Probability")
plt.ylabel("Count")
plt.title("Prediction Probability Distribution")
plt.legend()
plt.show()

thresholds = np.linspace(0, 1, 100)
accuracies = []

for t in thresholds:
    preds = (y_pred_probs > t).astype(int)
    acc = np.mean(preds.reshape(-1) == y_true)
    accuracies.append(acc)

plt.figure()
plt.plot(thresholds, accuracies)
plt.xlabel("Threshold")
plt.ylabel("Accuracy")
plt.title("Accuracy vs Decision Threshold")
plt.grid()
plt.show()
