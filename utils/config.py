from dotenv import load_dotenv
import os
import joblib

load_dotenv(override=True)

APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
SECRET_KEY_TOKEN = os.getenv("SECRET_KEY")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_DIR = os.path.join(BASE_DIR, 'models')

preprocessor = joblib.load(os.path.join(MODELS_DIR, 'preprocessor_pipeline.pkl'))
forest_model = joblib.load(os.path.join(MODELS_DIR, 'Random_forest_tuned.pkl'))
xgboost_model = joblib.load(os.path.join(MODELS_DIR, 'XGBoost_tuned.pkl'))
log_reg_model = joblib.load(os.path.join(MODELS_DIR, 'log_reg.pkl'))
