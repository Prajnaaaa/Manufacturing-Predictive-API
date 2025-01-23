# Manufacturing Predictive Analysis API

## Overview
This project is a RESTful API for predicting machine downtime or production defects in manufacturing operations using a simple machine learning model.

## Features
- Upload data in CSV format.
- Train a Logistic Regression model on the data.
- Predict machine downtime based on input features.

## Dataset
- **File**: `data/manufacturing_data.csv`
- **Columns**:
  - `Machine_ID`: Unique identifier for each machine.
  - `Temperature`: Operating temperature of the machine.
  - `Run_Time`: Machine runtime in hours.
  - `Downtime_Flag`: Indicates if downtime occurred (1 = Yes, 0 = No).

## Setup Instructions

### Prerequisites
- Python 3.7 or above.
- `pip` package manager.

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Manufacturing-Predictive-API
 
## Endpoints
1. Upload Data
Endpoint: POST /upload
Description: Upload a CSV file containing manufacturing data.
Input: File (CSV)

Example Request (cURL):
curl -X POST -F "file=@datasets/example_data.csv" http://127.0.0.1:5000/upload

Example Response:
{
  "message": "Data uploaded successfully",
  "columns": ["Machine_ID", "Temperature", "Run_Time", "Downtime_Flag"]
}

2. Train Model
Endpoint: POST /train
Description: Train the ML model on the uploaded data.
Example Request (cURL):
curl -X POST http://127.0.0.1:5000/train

Example:
{
  "message": "Model trained successfully",
  "accuracy": 0.85,
  "f1_score": 0.83
}

3. Predict
Endpoint: POST /predict
Description: Predict machine downtime using input features.
Input: JSON

Example Request (cURL):
curl -X POST -H "Content-Type: application/json" -d '{"Temperature": 75, "Run_Time": 100}' http://127.0.0.1:5000/predict

Example:
{
  "Downtime": "Yes",
  "Confidence": 0.85
}

## Testing
Use Postman or cURL to test the endpoints locally. Follow the examples provided above for accurate API interaction.
