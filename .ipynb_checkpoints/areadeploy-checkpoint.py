import streamlit as st
import pickle

model1=pickle.load(open("area.pkl","rb"))

def mydeploy():
    st.title("Area Price Prediction Model")

mydeploy()
     