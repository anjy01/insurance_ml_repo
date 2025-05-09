import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder, StandardScaler
import numpy as np
import pandas as pd


# load model artifacts
def load_artifacts():
    """ loads the model, encoder and scaler objects. """
    model = joblib.load('tips_model.pkl')
    label_encoders = joblib.load('label_encoders.pkl')
    scaler = joblib.load('scaler.pkl')

    return model, label_encoders, scaler

# get the model artifacts
model, label_encoders, scaler = load_artifacts()

# write a prediction function

def predict_charges(**data_dict):
    data_dict = {k:[v] for k, v in data_dict.items()}
    data = pd.DataFrame(data_dict)
    # encode the data
    cat_cols = ['sex','smoker','region']
    for col in cat_cols:
        data[col] = label_encoders[col].transform(data[col])
    data = scaler.transform(data)
    pred = model.predict(data)
    pred = f'The predicted insurance cost is ${pred[0]}'

    return pred

if __name__ == "__main__":
    print(predict_charges(age= 25, sex = "male", bmi = 33.5,
                    children = 2, smoker = "yes", region = "northeast"))