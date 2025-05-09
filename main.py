import streamlit as st 
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
from sklearn.ensemble import RandomForestRegressor

# load model artifacts
def load_artifacts():
    """ loads the model, encoder and scaler objects. """
    model = joblib.load('tips_model.pkl')
    label_encoders = joblib.load('label_encoders.pkl')
    scaler = joblib.load('scaler.pkl')
    
    return model, label_encoders, scaler

st.title('Insurance Charges Prediction Model')
st.divider()

column_1, column_2 = st.columns(2)
with column_1:
    age = st.number_input(label='age')
    sex = st.selectbox(label= 'sex', options= ['male', 'female'])
    smoker = st.selectbox(label= 'smoker', options=['yes', 'no'])

with column_2:
    regions = ['northeast', 'northwest', 'southeast', 'southwest']
    region = st.selectbox(label= 'region', options= regions)
    bmi = st.number_input(label= 'bmi')	
    children = st.number_input(label= 'children', max_value= 15, min_value= 0)
    
if st.button(label = 'predict'):
    st.divider()
    model, label_encoders, scaler = load_artifacts()
    data_dict = {
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    }
    
    data = pd.DataFrame(data_dict)
    # encode the data
    cat_cols = ['sex','smoker','region']
    for col in cat_cols:
        data[col] = label_encoders[col].transform(data[col])
    data = scaler.transform(data)
    pred = model.predict(data)
    st.success(f'The predicted insurance cost is ${pred[0]}')
