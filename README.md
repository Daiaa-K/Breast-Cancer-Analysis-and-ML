# Breast Cancer Analysis and ML API

This project provides a FastAPI-based machine learning API for predicting breast cancer using multiple models, including Random Forest, XGBoost, and Logistic Regression. The API accepts patient data as input and returns a prediction along with probability scores.

## Features
- **FastAPI** for building the RESTful API.
- **Multiple ML models** (Random Forest, XGBoost, Logistic Regression).
- **Data preprocessing** using a saved transformation pipeline.
- **Authentication** using API key validation.
- **CORS Middleware** for handling cross-origin requests.
- **Environment Variables** support using a `.env` file.
- **Docker support** for containerized deployment.

## Installation
### Prerequisites
Ensure you have Python 3.8 or later installed.

### Clone the Repository
```sh
git clone https://github.com/yourusername/breast-cancer-ml-api.git
cd breast-cancer-ml-api
```

### Install Dependencies
```sh
pip install -r requirements.txt
```

### Environment Setup
This project uses environment variables for configuration. Create a `.env` file in the root directory. An example `.env` file is provided as `.env.example`. Ensure it contains:
```ini
APP_NAME = 'Breast Cancer Analysis and ML'
VERSION = '1.0'
SECRET_KEY = 'your_secret_api_key_here'
```

### Running the API Locally
Start the FastAPI application using Uvicorn:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Usage
### Running with Docker
This project includes a `Dockerfile` to containerize the application. To build and run the Docker container:
```sh
docker build -t breast-cancer-api .
docker run -p 8000:8000 --env-file .env breast-cancer-api
```

### API Endpoints
#### Home
```http
GET /
```
Response:
```json
{
  "message": "Welcome to my app Breast Cancer Analysis and ML v1.0"
}
```

#### Predict Breast Cancer
##### Random Forest Model
```http
POST /predict/forest
```
##### XGBoost Model
```http
POST /predict/xgboost
```
##### Logistic Regression Model
```http
POST /predict/logreg
```
##### Request Body (Example):
```json
{
  "radius_mean": 14.2,
  "texture_mean": 20.1,
  "perimeter_mean": 91.5,
  "area_mean": 654.9,
  "smoothness_mean": 0.1,
  "compactness_mean": 0.12,
  "concavity_mean": 0.15,
  "concave_points_mean": 0.06,
  "symmetry_mean": 0.18,
  "radius_se": 0.4,
  "perimeter_se": 1.2,
  "area_se": 50.1,
  "compactness_se": 0.02,
  "concavity_se": 0.03,
  "concave_points_se": 0.01,
  "radius_worst": 17.5,
  "texture_worst": 25.6,
  "perimeter_worst": 112.2,
  "area_worst": 980.5,
  "smoothness_worst": 0.15,
  "compactness_worst": 0.21,
  "concavity_worst": 0.25,
  "concave_points_worst": 0.08,
  "symmetry_worst": 0.22,
  "fractal_dimension_worst": 0.08
}
```
##### Response Example:
```json
{
  "cancer_prediction": true,
  "cancer_probability": 0.89
}
```

## Authentication
Requests to prediction endpoints require an API key in the headers:
```http
X-API-Key: your_secret_api_key_here
```

## Folder Structure
```
📂 breast-cancer-ml-api
├── 📜 main.py            # FastAPI application
├── 📜 inference.py       # Prediction logic
├── 📜 PatientData.py     # Pydantic model for patient data
├── 📜 config.py          # Configuration and model loading
├── 📜 .env               # Environment variables (DO NOT SHARE)
├── 📜 requirements.txt   # Dependencies
├── 📜 Dockerfile         # Docker containerization
└── 📂 models             # Trained ML models
```

## License
This project is open-source and available under the MIT License.

## Authors
- Diaa_K

## Acknowledgments
- Dataset used for model training: [https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data]
- Libraries used: FastAPI, scikit-learn, XGBoost, Pandas, etc.

