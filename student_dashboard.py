import streamlit as st
import pandas as pd
import joblib
from data_preprocessing import data_preprocessing, encoder_Credit_Mix, encoder_Payment_Behaviour, encoder_Payment_of_Min_Amount
from prediction import prediction

col1, col2 = st.columns([1, 5])
with col1:
    st.image("https://github.com/dicodingacademy/assets/raw/main/logo.png", width=130)
with col2:
    st.header('Credit Scoring App (Prototype)')


data = pd.DataFrame()
 
col1, col2, col3 = st.columns(3)
 
with col1:
    Credit_Mix = st.selectbox(label='Credit_Mix', options=encoder_Credit_Mix.classes_, index=1)
    data["Credit_Mix"] = [Credit_Mix]
 
with col2:
    Payment_of_Min_Amount = st.selectbox(label='Payment_of_Min_Amount', options=encoder_Payment_of_Min_Amount.classes_, index=1)
    data["Payment_of_Min_Amount"] = [Payment_of_Min_Amount]
 
with col3:
    Payment_Behaviour = st.selectbox(label='Payment_Behaviour', options=encoder_Payment_Behaviour.classes_, index=5)
    data["Payment_Behaviour"] = Payment_Behaviour
 
