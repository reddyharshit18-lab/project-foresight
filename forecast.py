import streamlit as st
import pandas as pd

def show_forecast(model):

    st.title("🤖 AI Demand Forecast")

    day = st.number_input("Day",1,31,1)
    month = st.number_input("Month",1,12,7)
    week = st.number_input("Week",1,53,27)

    weekend = st.selectbox(
        "Weekend",
        ["No","Yes"]
    )

    weekend_value = 1 if weekend=="Yes" else 0

    lag1 = st.number_input(
        "Yesterday Sales",
        value=11.0
    )

    ma7 = st.number_input(
        "7-Day Average",
        value=10.5
    )

    if st.button("Predict"):

        future = pd.DataFrame({

            "Day":[day],
            "Month":[month],
            "Week":[week],
            "Weekend":[weekend_value],
            "M01AB_Lag1":[lag1],
            "M01AB_MA7":[ma7]

        })

        prediction = model.predict(future)

        st.success(
            f"Tomorrow Sales : {prediction[0]:.2f}"
        )