from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import APIKeyHeader 
from fastapi.middleware.cors import CORSMiddleware
from utils.config import APP_NAME, VERSION, SECRET_KEY_TOKEN, preprocessor, forest_model, xgboost_model, log_reg_model
from utils.PatientData import PatientData
from utils.inference import predict



app = FastAPI(title=APP_NAME, version=VERSION)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

api_key_header = APIKeyHeader(name = 'X-API-Key')

async def verify_api_key(api_key:str = Depends(api_key_header)):
    if api_key != SECRET_KEY_TOKEN:
        raise HTTPException(status_code=403, detail="You are not authorized to use this API")
    return api_key

@app.get("/", tags = ["Home"])
def home():
    return {"message": f"Welcome to my app {APP_NAME} v{VERSION}"}


@app.post("/predict/forest", tags = ["Predict"])
async def predict_forest(data:PatientData, api_key: str = Depends(verify_api_key)) -> dict:
    
    try:
        result = predict(data=data, preprocessor=preprocessor, model=forest_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))
    

@app.post("/predict/xgboost", tags = ["Predict"])
async def predict_forest(data:PatientData, api_key:str = Depends(verify_api_key)) -> dict:
    
    try:
        result = predict(data=data, preprocessor=preprocessor, model=xgboost_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))    
    
    
@app.post("/predict/logreg", tags = ["Predict"])
async def predict_forest(data:PatientData, api_key:str = Depends(verify_api_key)) -> dict:
    
    try:
        result = predict(data=data, preprocessor=preprocessor, model=log_reg_model)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))  