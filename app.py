# Import Libraries
import streamlit as st
import pickle
import pandas as pd 

# Define Heading
st.title("Salary Prediction Model 💼")
st.write("Enter your experience to predict your salary")

# Load the Model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# User Input
userInput = st.number_input("Experience Years", min_value=0.0, max_value=50.0, value=0.0, step=0.1)

# Predict Salary on Button Click
if st.button("Predict Salary"):

    experience = pd.DataFrame([[userInput]], columns=["Experience Years"])

    # Make the prediction
    prediction = model.predict(experience)
    
    # Display the result
    st.success(f"Estimated Salary: PKR {prediction[0][0]:,.0f}")
