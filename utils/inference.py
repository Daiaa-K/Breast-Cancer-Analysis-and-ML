import pandas as pd
from .PatientData import PatientData

def predict(data: PatientData,preprocessor,model):
    
    #processing Data
    new = pd.DataFrame([data.model_dump()])
    X_processed = preprocessor.transform(new)
    #predicting
    y_pred = model.predict(X_processed)
    y_proba = model.predict_proba(X_processed)
    
    return {
        "cancer_prediction": bool(y_pred[0]),
        "cancer_probability": float(y_proba[0][1])
    }
    