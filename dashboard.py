import streamlit as st
import plotly.express as px

def show_dashboard(sales):

    st.title("📊 Project FORESIGHT")
    st.subheader("AI-Powered Demand Forecasting & Inventory Intelligence")

    st.markdown("---")

    # Medicine Selection
    medicine = st.selectbox(
        "Select Medicine",
        [
            "M01AB",
            "M01AE",
            "N02BA",
            "N02BE",
            "N05B",
            "N05C",
            "R03",
            "R06"
        ]
    )

    # KPI Calculations
    total_sales = sales[medicine].sum()
    avg_sales = sales[medicine].mean()
    max_sales = sales[medicine].max()
    total_days = len(sales)

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Total Sales", f"{total_sales:.2f}")
    col2.metric("📈 Average Sales", f"{avg_sales:.2f}")
    col3.metric("🔥 Maximum Sales", f"{max_sales:.2f}")
    col4.metric("📅 Total Days", total_days)

    st.markdown("---")

    st.subheader("📋 Sales Dataset")

    st.dataframe(sales.head(10), use_container_width=True)

    st.markdown("---")

    st.subheader("📈 Daily Sales Trend")

    fig = px.line(
        sales,
        y=medicine,
        title=f"Daily Sales Trend - {medicine}"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    st.subheader("📊 Monthly Sales")

    monthly = sales.groupby("Month")[medicine].sum().reset_index()

    fig2 = px.bar(
        monthly,
        x="Month",
        y=medicine,
        title=f"Monthly Sales - {medicine}"
    )

    st.plotly_chart(fig2, use_container_width=True)