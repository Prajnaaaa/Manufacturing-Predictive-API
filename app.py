from flask import Flask, request, jsonify
import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score

app = Flask(__name__)

# Global variables to store the model and data
model = None
data = None

@app.route('/upload', methods=['POST'])
def upload_data():
    """Endpoint to upload a CSV file containing manufacturing data."""
    global data
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    try:
        data = pd.read_csv(file)
        return jsonify({"message": "Data uploaded successfully", "columns": list(data.columns)}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to read CSV file: {str(e)}"}), 500

@app.route('/train', methods=['POST'])
def train_model():
    """Endpoint to train the ML model using the uploaded dataset."""
    global model, data
    if data is None:
        return jsonify({"error": "No data uploaded. Please upload data first."}), 400

    try:
        # Assuming the dataset contains columns: 'Temperature', 'Run_Time', and 'Downtime_Flag'
        features = ['Temperature', 'Run_Time']
        target = 'Downtime_Flag'

        if not all(col in data.columns for col in features + [target]):
            return jsonify({"error": "Dataset missing required columns."}), 400

        X = data[features]
        y = data[target]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LogisticRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)

        # Save the trained model
        joblib.dump(model, 'model.pkl')

        return jsonify({"message": "Model trained successfully", "accuracy": accuracy, "f1_score": f1}), 200
    except Exception as e:
        return jsonify({"error": f"Failed to train model: {str(e)}"}), 500

@app.route('/predict', methods=['POST'])
def predict():
    """Endpoint to make a prediction using the trained model."""
    global model
    if model is None:
        try:
            model = joblib.load('model.pkl')
        except Exception:
            return jsonify({"error": "Model not trained yet. Please train the model first."}), 400

    try:
        input_data = request.get_json()
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400

        features = ['Temperature', 'Run_Time']
        input_df = pd.DataFrame([input_data])

        if not all(col in input_df.columns for col in features):
            return jsonify({"error": "Input data missing required features."}), 400

        prediction = model.predict(input_df[features])[0]
        confidence = max(model.predict_proba(input_df[features])[0])

        result = {"Downtime": "Yes" if prediction else "No", "Confidence": round(confidence, 2)}
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": f"Failed to make prediction: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
