import pandas as pd

def predict(data,preprocessor,model):
    
    X_processed = preprocessor.transform(data)
    
    y_pred = model.predict(X_processed)
    
    return y_pred
    