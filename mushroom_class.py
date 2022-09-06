import joblib
import pandas as pd
model_from_joblib=joblib.load('dtmodel.pkl')
def predict_mushroom_class(dataframe):
    r=model_from_joblib.predict(dataframe)
    return r


