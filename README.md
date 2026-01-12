# **Culex Mosquito Classifier**

A deep learning–based image classification system for distinguishing Culex mosquitoes from non-Culex species using RGB images.
This project focuses on binary classification, model evaluation, and performance analysis.

## Project Overview

Mosquito species identification is an important task in public health and disease prevention.
This project uses a Convolutional Neural Network (CNN) to classify mosquito images into:

**Culex**

**Non-Culex**

The model was trained on labeled <u>RGB images</u> and evaluated using standard classification metrics.

 ## Model Performance : 

🔹 **Confusion Matrix**

<img width="500" height="500" alt="B3V4_CONFUSION" src="https://github.com/user-attachments/assets/9f021d75-8b40-4cdd-b4ea-d94af23303f5" />

	

🔹 **Classification Report** : 

<img width="544" height="307" alt="image" src="https://github.com/user-attachments/assets/7bb661b9-6431-4725-8ac0-d564b0398423" />


**Overall Accuracy: 97%**

-Balanced performance across both classes

-Slightly higher recall for Non-Culex

-Strong precision for Culex, reducing false positives

## Dataset

The dataset consists of 5280 RGB mosquito images organized into two classes:

culex

non_culex

**Note:**
The dataset is not included in this repository due to size constraints.
If needed, the dataset structure is documented and can be shared upon request.

**Technologies Used**

-Python

-TensorFlow / Keras

-NumPy

-Matplotlib

-Scikit-learn

## Project Structure

20220859_CNN_Culex/
│

├── Back-END/

│   ├── app.py                  # Backend application (API)

│   ├── Database.py             # Database handling

│   ├── predictions.db          # SQLite database

│   ├── testing.py              # main functionality

│   ├── Wrong_Identifier.py     # Error analysis / misclassification handling

│   └── requirements.txt        # Backend dependencies

│

├── hard/                       # data labeled wrongly

│

├── public/#images & backgrounds

├── src/                        # Frontend source (React + Vite)

│   ├── assets/

│   ├── components/             # Reusable UI components

│   ├── services/               # API service calls

│   ├── App.jsx					#reaxt main app

│   ├── App.css					#main styles

│   ├── index.css

│   └── main.jsx

│

├── wrong_predictions_val/

│   └── culex_as_non_culex/      # Misclassified validation samples

│

├── Figures/                    # Evaluation plots for different volumes (ROC, PR, confusion matrix)

│

├── v6.py                       # CNN training script

├── evaluation.py               # Model evaluation & metrics

├── shufler.py                  # Dataset shuffling

│

├── index.html                  # Frontend entry point

├── package.json                # Frontend dependencies

├── package-lock.json

├── vite.config.js              # Vite configuration

├── eslint.config.js

│

├── .gitignore

└── README.md
this project contains one more embeded system for clarity

## Installation Requirements

Make sure you have the following installed on your system:

🔹**System Requirements**

Python 3.10

Node.js 18+ (for frontend)

pip (Python package manager)

npm (Node package manager)

🔹 **Backend Dependencies**

The backend uses **FastAPI** to serve the trained CNN model.

Install all required Python libraries using:


```python
pip install -r Back-END/requirements.txt

```

Required Python packages:

FastAPI – Backend API framework

Uvicorn – ASGI server to run FastAPI

TensorFlow – CNN model loading and inference

NumPy – Image preprocessing

Pillow – Image handling

python-multipart – Image upload support

🔹 **Frontend Dependencies**

Install frontend dependencies:

```bash
npm install
```

## How to Run the Model
1️⃣ Start the Backend (Model Inference API)
CMD:

```bash
cd Back-END
uvicorn app:app --reload
```

The CNN model is loaded automatically at startup

API will be available at:

**http://127.0.0.1:8000**


2️⃣ Start the Frontend 


```bash
npm run dev
```


Opens the web interface for image upload and prediction

3️⃣ Run Model Training (Optional)

If you want to retrain the CNN:
```bash
python v6.py
```

Trains the model on the dataset

Saves the trained model for inference

4️⃣ Evaluate the Model (Optional)

```bash
python evaluation.py
```

Generates:

Confusion matrix

ROC curve

Precision–Recall curve

Results are saved in the Figures/ directory.

 **Model saving location**
  The model will be saved in the model folder
  
Culex_Mosquito_Classifier\20220859_CNN_Culex\models

## Evaluation & Analysis

The project includes multiple evaluation figures, such as:

-ROC curve

-Precision–Recall curve

-Prediction distribution

-Decision threshold analysis

All figures are available in the Figures/ directory.

## Future Improvements

Addition of other species

Threshold optimization

Model explainability (Grad-CAM)

Deployment as a web or mobile application

## Author

**Emir Fenina**
