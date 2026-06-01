import os 
import urllib.request as request
from zipfile import ZipFile
import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity.config_entity import PrepareBaseModelConfig


class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config    


    def get_base_model(self):

        # Load pretrained VGG16 model without the top layers
        self.model = tf.keras.applications.vgg16.VGG16(
            input_shape = self.config.params_image_size,
            weights = self.config.params_weights,
            include_top = self.config.params_include_top
        )  

        self.save_model(
            path = self.config.base_model_path,
            model = self.model)  

    @staticmethod
    def _prepare_full_model(model,classes,learning_rate):

        # Freeze the layers of the base model
        for layer in model.layers[:-4]:
            layer.trainable = False
        
        # Add classification head to the base model
        
        flatten_in = tf.keras.layers.GlobalAveragePooling2D()(model.output)
        flatten_in = tf.keras.layers.Dropout(0.3)(flatten_in)
        prediction = tf.keras.layers.Dense(
            units=classes, 
            activation="softmax"
        )(flatten_in)

        full_model = tf.keras.Model(
            inputs=model.input, 
            outputs=prediction
            
        )

        full_model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=learning_rate),
            loss="CategoricalCrossentropy",
            metrics=[
                "accuracy",
                tf.keras.metrics.Precision(name="precision"),
                tf.keras.metrics.Recall(name="recall")]

        )

        full_model.summary()
        return full_model
    
    def update_base_model(self):

        full_model = self._prepare_full_model(
            model = self.model,
            classes = self.config.params_classes,
            learning_rate=self.config.params_learning_rate
        )

        self.save_model(
            path = self.config.updated_base_model_path,
            model = full_model
            )


    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)    