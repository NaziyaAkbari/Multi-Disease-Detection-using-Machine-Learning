import os
import numpy as np
import pickle
import json
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import (
    Conv2D, MaxPooling2D, Flatten, Dense,
    Dropout, BatchNormalization, GlobalAveragePooling2D
)
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.optimizers import Adam

IMG_SIZE = (224, 224)
BATCH_SIZE = 32

# ─────────────────────────────────────────────
# SKIN DISEASE MODEL
# ─────────────────────────────────────────────
def train_skin_model():
    print("\n===== Training Skin Disease Model =====")

    train_dir = 'diseases/datasets/skin/train'
    test_dir  = 'diseases/datasets/skin/test'

    train_gen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
        horizontal_flip=True,
        zoom_range=0.2,
        shear_range=0.1,
        fill_mode='nearest'
    )
    test_gen = ImageDataGenerator(rescale=1./255)

    train_data = train_gen.flow_from_directory(
        train_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )
    test_data = test_gen.flow_from_directory(
        test_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    # Save class labels
    class_labels = {v: k for k, v in train_data.class_indices.items()}
    os.makedirs('diseases/ml_models', exist_ok=True)
    with open('diseases/ml_models/skin_classes.json', 'w') as f:
        json.dump(class_labels, f)
    print("Skin classes:", class_labels)

    # Use MobileNetV2 as base (transfer learning)
    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    base_model.trainable = False  # freeze base

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(256, activation='relu'),
        BatchNormalization(),
        Dropout(0.5),
        Dense(128, activation='relu'),
        Dropout(0.3),
        Dense(len(class_labels), activation='softmax')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    callbacks = [
        EarlyStopping(patience=5, restore_best_weights=True),
        ModelCheckpoint(
            'diseases/ml_models/skin_model_best.h5',
            save_best_only=True, monitor='val_accuracy'
        )
    ]

    print("Training skin model...")
    history = model.fit(
        train_data,
        epochs=20,
        validation_data=test_data,
        callbacks=callbacks
    )

    # Evaluate
    loss, accuracy = model.evaluate(test_data)
    print(f"\nSkin Model Accuracy: {accuracy * 100:.2f}%")

    # Save final model
    model.save('diseases/ml_models/skin_model.h5')
    print("Skin model saved to diseases/ml_models/skin_model.h5")
    return accuracy


# ─────────────────────────────────────────────
# CHICKENPOX MODEL
# ─────────────────────────────────────────────
def train_chickenpox_model():
    print("\n===== Training Chickenpox Model =====")

    train_dir = 'diseases/datasets/chickenpox/train'
    test_dir  = 'diseases/datasets/chickenpox/test'

    train_gen = ImageDataGenerator(
        rescale=1./255,
        rotation_range=15,
        width_shift_range=0.1,
        height_shift_range=0.1,
        horizontal_flip=True,
        zoom_range=0.15,
        fill_mode='nearest'
    )
    test_gen = ImageDataGenerator(rescale=1./255)

    train_data = train_gen.flow_from_directory(
        train_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )
    test_data = test_gen.flow_from_directory(
        test_dir,
        target_size=IMG_SIZE,
        batch_size=BATCH_SIZE,
        class_mode='categorical'
    )

    # Save class labels
    class_labels = {v: k for k, v in train_data.class_indices.items()}
    with open('diseases/ml_models/chickenpox_classes.json', 'w') as f:
        json.dump(class_labels, f)
    print("Chickenpox classes:", class_labels)

    base_model = MobileNetV2(
        weights='imagenet',
        include_top=False,
        input_shape=(224, 224, 3)
    )
    base_model.trainable = False

    model = Sequential([
        base_model,
        GlobalAveragePooling2D(),
        Dense(128, activation='relu'),
        BatchNormalization(),
        Dropout(0.4),
        Dense(64, activation='relu'),
        Dropout(0.3),
        Dense(len(class_labels), activation='softmax')
    ])

    model.compile(
        optimizer=Adam(learning_rate=0.001),
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    callbacks = [
        EarlyStopping(patience=5, restore_best_weights=True),
        ModelCheckpoint(
            'diseases/ml_models/chickenpox_model_best.h5',
            save_best_only=True, monitor='val_accuracy'
        )
    ]

    print("Training chickenpox model...")
    history = model.fit(
        train_data,
        epochs=20,
        validation_data=test_data,
        callbacks=callbacks
    )

    loss, accuracy = model.evaluate(test_data)
    print(f"\nChickenpox Model Accuracy: {accuracy * 100:.2f}%")

    model.save('diseases/ml_models/chickenpox_model.h5')
    print("Chickenpox model saved.")
    return accuracy


if __name__ == '__main__':
    skin_acc = train_skin_model()
    chkpx_acc = train_chickenpox_model()
    print("\n========== Training Complete ==========")
    print(f"Skin Disease Model Accuracy    : {skin_acc*100:.2f}%")
    print(f"Chickenpox Model Accuracy      : {chkpx_acc*100:.2f}%")