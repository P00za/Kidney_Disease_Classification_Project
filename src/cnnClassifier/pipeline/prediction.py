import os
import numpy as np
import tensorflow as tf

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input


class PredictionPipeline:

    def __init__(self, filename):

        # Path of uploaded image
        self.filename = filename

        # Path of trained model
        self.model_path = os.path.join(
            "model",
            "trained_model.h5"
        )

        # Class labels
        self.class_labels = {
            0: "Cyst",
            1: "Normal",
            2: "Stone",
            3: "Tumor"
        }

        # Load trained model only once
        self.model = load_model(self.model_path)


    def preprocess_image(self):

        """
        Load and preprocess image for prediction
        """

        # Load image
        img = image.load_img(
            self.filename,
            target_size=(224, 224)
        )

        # Convert image to numpy array
        img_array = image.img_to_array(img)

        # Add batch dimension
        img_array = np.expand_dims(img_array, axis=0)

        # IMPORTANT:
        # VGG16 preprocessing
        img_array = preprocess_input(img_array)

        return img_array


    def predict(self):

        """
        Predict kidney disease class
        """

        # Preprocess image
        processed_image = self.preprocess_image()

        # Model prediction probabilities
        predictions = self.model.predict(processed_image)

        # Predicted class index
        predicted_class_index = np.argmax(predictions, axis=1)[0]

        # Prediction confidence
        confidence = float(np.max(predictions) * 100)

        # Predicted class label
        predicted_label = self.class_labels[predicted_class_index]

        # Convert probabilities into percentage
        probabilities = {
            self.class_labels[i]: round(float(predictions[0][i] * 100), 2)
            for i in range(len(self.class_labels))
        }

        # Final output
        result = {
            "prediction": predicted_label,
            "confidence": round(confidence, 2),
            "probabilities": probabilities
        }

        return result