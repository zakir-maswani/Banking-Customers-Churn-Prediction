import streamlit as st
import pandas as pd
import pickle

st.title("Banking Customer Churn Prediction")

sidebar_title = st.sidebar.title("Input Features")

CreditScore = st.sidebar.number_input("Enter Credit Score:", min_value=350, max_value=850)
Geography = st.sidebar.selectbox(
    "Enter Geography:",
    ["France","Spain", "Germany"]
)
Gender = st.sidebar.selectbox(
    "Chooce Gender",
    ["Male", "Female"]
)
Age = st.sidebar.number_input("Enter Age:", min_value=18, max_value=92)
Tenure = st.sidebar.number_input("Enter Tenure:", max_value=10)
Balance = st.sidebar.number_input("Enter balance:", max_value=250898)
NumOfProducts = st.sidebar.number_input("Enter the Number of Products:", min_value=1, max_value=4)
HasCrCard = st.sidebar.number_input("Has Card: ", min_value=0, max_value=1)
IsActiveMember = st.sidebar.number_input("Is Active Memeber: ", min_value=0, max_value=1)
EstimatedSalary = st.sidebar.number_input("Enter Estimated Salar:", min_value=11.58, max_value=199992.48)

df = pd.DataFrame({
    "CreditScore": [CreditScore],
    "Geography": [Geography],
    "Gender": [Gender],
    "Age": [Age],
    "Tenure": [Tenure],
    "Balance": [Balance],
    "NumOfProducts": [NumOfProducts],
    "HasCrCard": [HasCrCard],
    "IsActiveMember": [IsActiveMember],
    "EstimatedSalary": [EstimatedSalary]
})
st.write("Input Data")
st.write(df.head())

df["Geography"] = df["Geography"].map({"France": 1, "Spain": 2, "Germany": 3})
df["Gender"] = df["Gender"].map({"Male": 1, "Female": 0})


with open("Model.pkl", "rb") as file:
    model = pickle.load(file)

prediction = model.predict(df)

if prediction == 1:
    st.write("At risk")

else:
    st.write("Customer Retained")
