from flask import Flask, request, jsonify
from model import probe_model_5l_profit
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def lading():
    return "Server is live",200

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get JSON data from the POST request
        data = request.get_json()

        # Validate that the necessary data is present
        if not data or 'data' not in data:
            return jsonify({"error": "Invalid input format, 'data' key missing or no data provided"}), 400

        # Call the model function with the provided data
        result = probe_model_5l_profit(data['data'])

        # Return the result as a JSON response
        return jsonify(result), 200

    except Exception as e:
        # Return an error message in case of failure
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
