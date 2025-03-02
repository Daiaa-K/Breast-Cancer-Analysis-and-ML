from dotenv import load_dotenv
import os

load_dotenv(Override=True)

APP_NAME = os.getenv("APP_NAME")
VERSION = os.getenv("VERSION")
SECRET_KEY_TOKEN = os.getenv("SECRET_KEY")

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODELS_DIR = os.path.join(BASE_DIR, 'models')

preprocessor = os.path.join(MODELS_DIR, 'preprocessor_pipeline.pkl')
forest_model = os.path.join(MODELS_DIR, 'Random_forest_tuned.pkl')
xgboost_model = os.path.join(MODELS_DIR, 'XGBoost_tuned.pkl')
log_reg_model = os.path.join(MODELS_DIR, 'log_reg.pkl')