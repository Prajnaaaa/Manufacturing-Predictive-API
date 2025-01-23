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
