import streamlit as st
import pandas as pd
import joblib

from dashboard import show_dashboard
from forecast import show_forecast
from inventory import show_inventory
from about import show_about

st.set_page_config(
    page_title="Project FORESIGHT",
    layout="wide"
)

sales = pd.read_csv("data/feature_engineered_sales.csv")
inventory = pd.read_csv("data/inventory_report.csv")
model = joblib.load("model.pkl")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Forecast",
        "Inventory",
        "About"
    ]
)

if page=="Dashboard":
    show_dashboard(sales)

elif page=="Forecast":
    show_forecast(model)

elif page=="Inventory":
    show_inventory(inventory)

else:
    show_about()