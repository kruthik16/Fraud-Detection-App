import streamlit as st
import pandas as pd
import joblib

model= joblib.load("fraud_detection_pipeline.pkl")
st.title("Fraud Detection Prediction App")
st.markdown("please neter the transaction details and use the predict button")
st.divider()
transaction_type=st.selectbox("Transaction Type",["PAYMENT","TRANSFER","CASH_OUT","DEPOSIT"])
amount=st.number_input("Amount",min_value=0.0,value=1000.00)
oldbalanceOrg=st.number_input("Old Balance(Sender)",min_value=0.0,value=1000.00)
newbalanceOrig=st.number_input("New Balance(Sender)",min_value=0.0,value=9000.00)
oldbalanceDest=st.number_input("Old Balance(Receiver)",min_value=0.0,value=0.0)
newbalanceDest=st.number_input("New Balance(Receiver)",min_value=0.0,value=0.0)

if st.button("Predict"):
    input_data=pd.DataFrame([{
        "type":transaction_type,
        "amount":amount,
        "oldbalanceOrg":oldbalanceOrg,
        "newbalanceOrig": newbalanceOrig, 
        "oldbalanceDest":oldbalanceDest,
        "newbalanceDest": newbalanceDest 

    }])
    

    prediction=model.predict(input_data)[0]
    st.subheader(f"Prediction : '{ int(prediction)}'")

    if prediction ==1:
        st.error("This Transaction can be Fraud")
    else:
        st.success("This Transaction looks like not a Fraud") 


