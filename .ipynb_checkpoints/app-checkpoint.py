import streamlit as st
import pickle

model1=pickle.load(open("area.pkl","rb"))

def mydeploy():
    st.title("Area Price Prediction Model")
    area=st.number_input("Enter the value of area : ")
    pred=st.button("predict price")
    if pred:
        predi=model1.predict([[area]])
        st.write("price of area is : ",predi[0])

mydeploy()
     