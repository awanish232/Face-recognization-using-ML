from flask import Flask, render_template, request, jsonify
from keras.models import load_model
import cv2
import numpy as np

app = Flask(__name__)

# Load the trained model
model = load_model("emotiondetector.h5")

# Define route to render the web page
@app.route('/')
def index():
    return render_template('index.html')

# Define route for predictions
@app.route('/predict', methods=['POST'])
def predict():
    image_data = request.get_data()
    # Process image_data using cv2 and the loaded model
    # Example code: (Note: This is a simplified example, you may need to adapt it)
    image_array = np.frombuffer(image_data, dtype=np.uint8)
    image = cv2.imdecode(image_array, cv2.IMREAD_GRAYSCALE)
    image = cv2.resize(image, (48, 48))
    image = image.reshape(1, 48, 48, 1)
    image = image / 255.0
    prediction = model.predict(image)
    predicted_class = np.argmax(prediction)
    predicted_emotion = ['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise'][predicted_class]
    return jsonify({'emotion': predicted_emotion})

if __name__ == '__main__':
    app.run(debug=True)
