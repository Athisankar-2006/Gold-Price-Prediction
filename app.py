# # flask for serverside


# from flask import Flask, request, jsonify
# import pickle
# import numpy as np

# app = Flask(__name__)

# # Load model & scaler
# model = pickle.load(open("regression.pkl", "rb"))
# scaler = pickle.load(open("scaler.pkl", "rb"))

# @app.route("/")
# def home():
#     return "Gold Price Prediction API is running"

# @app.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()

#     usd_inr = float(data["USD_INR"])

#     # Scale input (VERY IMPORTANT)
#     usd_inr_scaled = scaler.transform([[usd_inr]])

#     # Predict
#     prediction = model.predict(usd_inr_scaled)

#     return jsonify({
#         "predicted_gold_price": round(prediction[0], 2)
#     })

# if __name__ == "__main__":
#     app.run(debug=True)





import os
from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# get current file directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, "regression.pkl")
scaler_path = os.path.join(BASE_DIR, "scaler.pkl")

# load model & scaler
model = pickle.load(open(model_path, "rb"))
scaler = pickle.load(open(scaler_path, "rb"))

@app.route("/")
def home():
    return "Gold Price Prediction API is running"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    usd_inr = float(data["USD_INR"])

    usd_inr_scaled = scaler.transform([[usd_inr]])
    prediction = model.predict(usd_inr_scaled)[0]
     
    prediction_rounded=round(float(prediction), 2)

    return jsonify({
        "predicted_gold_price": prediction_rounded
    })

if __name__ == "__main__":
    app.run(debug=True ,host="0.0.0.0",port=8080)
