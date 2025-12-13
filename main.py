import streamlit as st 
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import joblib
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
# load model artifacts
@st.cache_resource
def load_artifacts():
    """ loads the model, encoder and scaler objects. """
    model = joblib.load(BASE_DIR/ 'tips_model.pkl')
    label_encoders = joblib.load(BASE_DIR/ 'label_encoders.pkl')
    scaler = joblib.load(BASE_DIR/ 'scaler.pkl')
    
    return model, label_encoders, scaler

st.title('💵 Insurance Charges Prediction Model')
st.write(
    """
    This application predicts insurance charges using a trained machine learning model.
    Input client details to get an estimated Insurance Charge.
    """
)
st.divider()

column_1, column_2 = st.columns(2)
with column_1:
    age = st.number_input("Age", min_value=18, max_value=100)
    sex = st.selectbox(label= 'sex', options= ['male', 'female'])
    smoker = st.selectbox(label= 'smoker', options=['yes', 'no'])

with column_2:
    region = st.selectbox("Region",
        ["northeast", "northwest", "southeast", "southwest"]
    )
    bmi = st.number_input("BMI", min_value=5.0, max_value=80.0)
    children = st.number_input(label= 'children', max_value= 50, min_value= 0)
    
if st.button('Predict'):
    st.divider()
    model, label_encoders, scaler = load_artifacts()
    data = pd.DataFrame({
        'age': [age],
        'sex': [sex],
        'bmi': [bmi],
        'children': [children],
        'smoker': [smoker],
        'region': [region]
    })
    
    # encode the data
    cat_cols = ['sex','smoker','region']
    for col in cat_cols:
        if data[col][0] not in label_encoders[col].classes_:
            st.error(f"Unknown category for {col}")
            st.stop()
        data[col] = label_encoders[col].transform(data[col])
    data_scaled = scaler.transform(data)
    pred = model.predict(data_scaled)
    st.metric(
        label="Predicted Insurance Cost",
        value=f"${pred[0]:,.2f}"
    )
