import os
import numpy as np
import json
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
import time
from sklearn.utils.class_weight import compute_class_weight
from cnnClassifier.entity.config_entity import TrainingConfig
from pathlib import Path
from tensorflow.keras.applications.vgg16 import preprocess_input


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )

    
    def train_valid_generator(self):

        # validation generator

        valid_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_input,
            validation_split=0.20
        )

        # Training generator

        train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
            preprocessing_function=preprocess_input,
            validation_split=0.20,
            rotation_range = 10,
            zoom_range = 0.1,
            horizontal_flip = True,
            brightness_range = [0.9,1.1]

        )


        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
            class_mode="categorical"
            
        )

        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear",
            class_mode="categorical"
        )

        # Training Data
        self.train_generator = train_datagen.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )

        # Validation Data

        self.valid_generator = valid_datagen.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )

        # save class labels
        with open("artifacts/class_indices.json", "w") as f:
            json.dump(self.train_generator.class_indices, f)


        print(" Class mapping: ")
        print(self.train_generator.class_indices)

        # Compute class weights
        class_weights = compute_class_weight(
            class_weight="balanced",
            classes=np.unique(self.train_generator.classes),
            y=self.train_generator.classes
        ) 

        self.class_weights = dict(enumerate(class_weights))

        print("Class weights: ")
        print(self.class_weights)


    def train(self):

        callbacks = [

            tf.keras.callbacks.EarlyStopping(
                monitor="val_loss",
                patience=5,
                restore_best_weights=True
            ),

            tf.keras.callbacks.ReduceLROnPlateau(
                monitor="val_loss",
                factor=0.2,
                patience=3,
                verbose=1
            )  ,

            tf.keras.callbacks.ModelCheckpoint(
                filepath = "artifacts/training/best_model.h5",
                save_best_only=True,
                monitor = 'val_accuracy',
            ) 
        ]

        history = self.model.fit(
            self.train_generator,
            validation_data=self.valid_generator,
            epochs=self.config.params_epochs,
            class_weight=self.class_weights,
            callbacks=callbacks
        )

        # Save the final trained model

        self.model.save(self.config.trained_model_path)

