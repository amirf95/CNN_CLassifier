import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
#from tensorflow.keras.applications import EfficientNetB0 #B0 model
from tensorflow.keras.applications import EfficientNetB3 #B3 model
from tensorflow.keras.applications.efficientnet import preprocess_input

#==== Clear previous sessions====
tf.keras.backend.clear_session()
# ===== MODEL DEFINITION =====
base_model = EfficientNetB3(
    weights='imagenet',#use learned knowledge
    include_top=False,#remove Imagenet classifier
    #input_shape=(224, 224, 3)#for B0
    input_shape=(300, 300, 3)#for B3
)
#freeze base model to not forget what it learned “Don’t touch the brain, only teach the decision.”  
base_model.trainable = False

"""
    Training from scratch architecture:
    keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(224,224,3)),
    keras.layers.MaxPooling2D(2,2),

    keras.layers.Conv2D(64, (3,3), activation='relu'),
    keras.layers.MaxPooling2D(2,2),

    keras.layers.Conv2D(128, (3,3), activation='relu'),
    keras.layers.MaxPooling2D(2,2),

    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')  # ✅ binary
    """
# ====Build the complete model====
model = keras.Sequential([
    
     base_model,

    keras.layers.GlobalAveragePooling2D(),
    keras.layers.BatchNormalization(),

    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.3),

    keras.layers.Dense(1, activation='sigmoid') 
])
# ===== HYPERPARAMETERS =====
DATASET_DIR = r'C:\Users\amirf\Downloads\dataset'#datasset path
BATCH_SIZE = 16#batch size for training and validation : 16
class_weight = {
    0: 1.2,  # non_culex (penalize mistakes more)
    1: 1.0   # culex
}

# ===== DATA PREPARATION =====
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    # Data augmentation
    rotation_range=10,
    width_shift_range=0.05,
    height_shift_range=0.05,
    zoom_range=0.1,
    horizontal_flip=True,
    # 15% for validation
    validation_split=0.15 
)
# Validation data generator (no augmentation)
val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input, # no augmentation for validation
    validation_split=0.15 # 15% for validation
    )
# ====Generators====
train_dataset = train_datagen.flow_from_directory(
    DATASET_DIR,
    #target_size=(224,224),
    target_size=(300,300),#for B3
    color_mode='rgb',
    batch_size=8,
    class_mode='binary',
    subset='training',
    shuffle=True,
    seed=42
)

val_dataset = val_datagen.flow_from_directory(
    DATASET_DIR,
    #target_size=(224,224),
    target_size=(300,300),#for B3
    color_mode='rgb',
    batch_size=16,
    class_mode='binary',
    subset='validation',
    shuffle=False,
    seed=42 # for reproducibility
)

# ===== MODEL COMPILATION AND TRAINING =====
model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-4),
    loss='binary_crossentropy',
    metrics=['accuracy']
)
# Callbacks
early_stop = EarlyStopping(
    monitor='val_loss',
    patience=2,
    restore_best_weights=True
)
# ====Save best model====
checkpoint = ModelCheckpoint(
    'C:\\Users\\amirf\\OneDrive\\Desktop\\Culex_Mosquito_Classifier\\models\\best_culex_binary_RGB_V4.keras',
    monitor='val_loss',
    save_best_only=True
)

# Initial training of the top layers
history_1=model.fit(
    train_dataset,
    epochs=10,
    validation_data=val_dataset,
    callbacks=[early_stop, checkpoint],
    class_weight=class_weight
)

# Fine-tuning: unfreeze some layers of the base model
base_model.trainable = True
# Unfreeze the last 30 layers
for layer in base_model.layers[:-30]:
    layer.trainable = False
model.compile(
    optimizer=keras.optimizers.Adam(1e-5),# lower learning rate
    loss='binary_crossentropy',#binary classification
    metrics=[
        'accuracy',
        tf.keras.metrics.Precision(name='precision'),
        tf.keras.metrics.Recall(name='recall')
]
)
# Continue training with fine-tuning
history_2=model.fit(
    train_dataset,  
    epochs=3,#number of epochs
    validation_data=val_dataset,
    callbacks=[early_stop, checkpoint],
    class_weight=class_weight
)
# Save the final model
model.save('C:\\Users\\amirf\\OneDrive\\Desktop\\Culex_Mosquito_Classifier\\models\\culex_binary_RGB_V4.keras')

