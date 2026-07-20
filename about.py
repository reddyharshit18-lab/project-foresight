import streamlit as st

def show_about():

    st.title("ℹ️ About Project")

    st.markdown("---")

    st.header("📊 Project FORESIGHT")

    st.write("""
Project FORESIGHT is an AI-powered Demand Forecasting and Inventory Intelligence Platform.

The project predicts future medicine demand using Machine Learning and helps businesses make better inventory decisions.
""")

    st.markdown("---")

    st.header("🎯 Objectives")

    st.write("""
✔ Predict future medicine sales

✔ Reduce stockout risk

✔ Reduce overstock

✔ Improve inventory planning

✔ Help businesses make data-driven decisions
""")

    st.markdown("---")

    st.header("🛠 Technologies Used")

    st.write("""
- Python

- Pandas

- NumPy

- Scikit-Learn

- Streamlit

- Plotly

- Machine Learning

- Joblib
""")

    st.markdown("---")

    st.header("📂 Dataset")

    st.write("""
Dataset contains:

• Daily Medicine Sales

• Month

• Week

• Weekend

• Previous Day Sales

• Moving Average

• Inventory Status
""")

    st.markdown("---")

    st.header("👨‍🎓 Developed By")

    st.write("""
Harshit

PGDM (Data Science & Business Analytics)

ISBR Business School
""")

    st.markdown("---")

    st.success("Project FORESIGHT Version 1.0")