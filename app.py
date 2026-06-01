from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin

import os
import traceback

from cnnClassifier.utils.Common import decodeImage
from cnnClassifier.pipeline.prediction import PredictionPipeline


# ---------------------------------------------------------
# Set Environment Variables
# ---------------------------------------------------------

os.putenv("LANG", "en_US.UTF-8")
os.putenv("LC_ALL", "en_US.UTF-8")


# ---------------------------------------------------------
# Initialize Flask App
# ---------------------------------------------------------

app = Flask(__name__)

CORS(app)


# ---------------------------------------------------------
# Client Application Class
# ---------------------------------------------------------

class ClientApp:

    def __init__(self):

        # Uploaded image temporary filename
        self.filename = "inputImage.jpg"

        # Prediction pipeline object
        self.classifier = PredictionPipeline(
            self.filename
        )


# Create app object
clApp = ClientApp()


# ---------------------------------------------------------
# Home Route
# ---------------------------------------------------------

@app.route("/", methods=["GET"])
@cross_origin()

def home():

    """
    Render homepage
    """

    return render_template("index.html")


# ---------------------------------------------------------
# Training Route
# ---------------------------------------------------------

@app.route("/train", methods=["GET", "POST"])
@cross_origin()

def trainRoute():

    """
    Trigger complete DVC pipeline training
    """

    try:

        os.system("dvc repro")

        return jsonify({

            "status": "success",
            "message": "Training completed successfully"

        })

    except Exception as e:

        return jsonify({

            "status": "error",
            "message": str(e)

        })


# ---------------------------------------------------------
# Prediction Route
# ---------------------------------------------------------

@app.route("/predict", methods=["POST"])
@cross_origin()

def predictRoute():

    """
    Predict kidney disease class
    """

    try:

        # Check request data
        data = request.get_json()

        if data is None:

            return jsonify({

                "status": "error",
                "message": "No JSON data received"

            })

        # Check image key
        if "image" not in data:

            return jsonify({

                "status": "error",
                "message": "Image key missing"

            })

        # Base64 image
        image_data = data["image"]

        # Decode and save image
        decodeImage(
            image_data,
            clApp.filename
        )

        # Perform prediction
        result = clApp.classifier.predict()

        # Return prediction result
        return jsonify({

            "status": "success",
            "prediction": result["prediction"],
            "confidence": result["confidence"],
            "probabilities": result["probabilities"]

        })

    except Exception as e:

        print(traceback.format_exc())

        return jsonify({

            "status": "error",
            "message": str(e)

        })


# ---------------------------------------------------------
# Main Function
# ---------------------------------------------------------

if __name__ == "__main__":

    # Run Flask App

    app.run(

        host="0.0.0.0",
        port=8080,
        debug=True

    )