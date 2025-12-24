🦟 Culex Mosquito Classifier

A deep learning–based image classification system for distinguishing Culex mosquitoes from non-Culex species using RGB images.
This project focuses on binary classification, model evaluation, and performance analysis.

📌 Project Overview

Mosquito species identification is an important task in public health and disease prevention.
This project uses a Convolutional Neural Network (CNN) to classify mosquito images into:

Culex

Non-Culex

The model was trained on labeled RGB images and evaluated using standard classification metrics.

🧠 Model Performance
🔹 Confusion Matrix
[[251  35]
 [ 58 221]]

	Predicted Non-Culex	Predicted Culex
Actual Non-Culex	251	35
Actual Culex	58	221
🔹 Classification Report
Class	Precision	Recall	F1-score	Support
Non-Culex	0.81	0.88	0.84	286
Culex	0.86	0.79	0.83	279
Accuracy			0.84	565

Overall Accuracy: 84%

Balanced performance across both classes

Slightly higher recall for Non-Culex

Strong precision for Culex, reducing false positives

📊 Evaluation & Analysis

The project includes multiple evaluation figures such as:

ROC curve

Precision–Recall curve

Prediction distribution

Decision threshold analysis

All figures are available in the Figures/ directory.

📂 Project Structure
Culex_Mosquito_Classifier/
│
├── src/
│   ├── v6.py              # Model training
│   ├── testing.py         # Inference and testing
│   └── evaluation.py     # Metrics and plots
│
├── Figures/               # Evaluation plots
│
├── .gitignore             # Ignore dataset & large files
└── README.md

📁 Dataset

The dataset consists of RGB mosquito images organized into two classes:

culex

non_culex

⚠️ Note:
The dataset is not included in this repository due to size constraints.
If needed, the dataset structure is documented and can be shared upon request.

⚙️ Technologies Used

Python

TensorFlow / Keras

NumPy

Matplotlib

Scikit-learn

🚀 Future Improvements

Data augmentation and class balancing

Threshold optimization

Transfer learning (EfficientNet / ResNet)

Model explainability (Grad-CAM)

Deployment as a web or mobile application

👤 Author

Emir Fenina
