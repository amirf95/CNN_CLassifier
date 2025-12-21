import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.applications import EfficientNetB0
from tensorflow.keras.applications.efficientnet import preprocess_input

tf.keras.backend.clear_session()
# ===== MODEL DEFINITION =====
base_model = EfficientNetB0(
    weights='imagenet',#use learned knowledge
    include_top=False,#remove Imagenet classifier
    input_shape=(224, 224, 3)
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
model = keras.Sequential([
    
     base_model,

    keras.layers.GlobalAveragePooling2D(),
    keras.layers.BatchNormalization(),

    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dropout(0.3),

    keras.layers.Dense(1, activation='sigmoid') 
])
train_dir = 'C:\\Users\\amirf\\OneDrive\\Desktop\\Culex_Mosquito_Classifier\\data\\Train'
val_dir   = 'C:\\Users\\amirf\\OneDrive\\Desktop\\Culex_Mosquito_Classifier\\data\\Val'



train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=10,
    width_shift_range=0.05,
    height_shift_range=0.05,
    zoom_range=0.1,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input
    )
train_dataset = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224,224),
    color_mode='rgb',
    batch_size=16,
    class_mode='binary'
)

val_dataset = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224,224),
    color_mode='rgb',
    batch_size=16,
    class_mode='binary'
)

model.compile(
    optimizer=keras.optimizers.Adam(learning_rate=1e-4),
    loss='binary_crossentropy',
    metrics=['accuracy']
)

early_stop = EarlyStopping(
    monitor='val_loss',
    patience=3,
    restore_best_weights=True
)

checkpoint = ModelCheckpoint(
    'C:\\Users\\amirf\\OneDrive\\Desktop\\Culex_Mosquito_Classifier\\models\\best_culex_binary_RGB.keras',
    monitor='val_loss',
    save_best_only=True
)


history_1=model.fit(
    train_dataset,
    epochs=10,
    validation_data=val_dataset,
    callbacks=[early_stop, checkpoint]
)

base_model.trainable = True

for layer in base_model.layers[:-30]:
    layer.trainable = False
model.compile(
    optimizer=keras.optimizers.Adam(1e-5),
    loss='binary_crossentropy',
    metrics=['accuracy']
)
history_2=model.fit(
    train_dataset,  
    epochs=10,
    validation_data=val_dataset,
    callbacks=[early_stop, checkpoint]
)

model.save('C:\\Users\\amirf\\OneDrive\\Desktop\\Culex_Mosquito_Classifier\\models\\culex_binary_RGB.keras')

