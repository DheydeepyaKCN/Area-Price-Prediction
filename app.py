import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("area_price_model.pkl", "rb"))

# Page configuration
st.set_page_config(
    page_title="Area Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# Title
st.title("🏠 Area Price Prediction")

st.write(
    "Predict the estimated house price based on the area using a trained Linear Regression model."
)

st.divider()

# User Input
area = st.number_input(
    "📏 Enter Area (sq. ft.)",
    min_value=100,
    max_value=10000,
    value=1000,
    step=100
)

# Prediction
if st.button("💰 Predict Price", use_container_width=True):
    prediction = model.predict([[area]])
    st.success(f"Estimated House Price: ₹ {prediction[0]:,.2f}")

st.divider()

# Footer
st.caption("Built with Python • Scikit-learn • Streamlit")