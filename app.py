import streamlit as st
import pickle
import numpy as np

# Load the model (ensure model.pkl is in the same directory or provide the path)
model = pickle.load(open('model.pkl', 'rb'))

# Streamlit UI
st.title('Mobile Phone Feature Prediction')

st.write("Enter the mobile phone features to predict the target value:")

# Input fields for the features
battery_power = st.number_input("Battery Power", min_value=0, max_value=10000)
clock_speed = st.number_input("Clock Speed", min_value=0.0, max_value=5.0)
dual_sim = st.selectbox("Dual SIM", ["Yes", "No"])
int_memory = st.number_input("Internal Memory", min_value=0, max_value=128)
ram = st.number_input("RAM", min_value=0, max_value=16)

# Convert dual_sim to binary (1 for Yes, 0 for No)
dual_sim = 1 if dual_sim == "Yes" else 0

# Prepare input for model (reshape to match expected input format)
input_data = np.array([[battery_power, clock_speed, dual_sim, int_memory, ram]])

# Prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted range: {prediction[0]}')

