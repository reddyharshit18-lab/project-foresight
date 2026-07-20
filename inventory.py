import streamlit as st
import plotly.express as px

def show_inventory(inventory):

    st.title("📦 Inventory Intelligence Dashboard")

    st.markdown("---")

    # ===========================
    # KPI Cards
    # ===========================

    total = len(inventory)
    healthy = len(inventory[inventory["Status"] == "Healthy"])
    stockout = len(inventory[inventory["Status"] == "Stockout Risk"])
    overstock = len(inventory[inventory["Status"] == "Overstock"])

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💊 Total Medicines", total)
    col2.metric("🟢 Healthy", healthy)
    col3.metric("🔴 Stockout Risk", stockout)
    col4.metric("🟡 Overstock", overstock)

    st.markdown("---")

    # ===========================
    # Inventory Table
    # ===========================

    st.subheader("📋 Inventory Report")

    st.dataframe(inventory, use_container_width=True)

    st.markdown("---")

    # ===========================
    # Medicine Filter
    # ===========================

    medicine = st.selectbox(
        "Select Medicine",
        inventory["Medicine"]
    )

    filtered = inventory[inventory["Medicine"] == medicine]

    st.dataframe(filtered, use_container_width=True)

    st.markdown("---")

    # ===========================
    # Stock Status
    # ===========================

    status = filtered.iloc[0]["Status"]

    if status == "Healthy":
        st.success("🟢 Healthy Inventory")

    elif status == "Stockout Risk":
        st.error("🔴 Immediate Reorder Required")

    else:
        st.warning("🟡 Overstock - Reduce Inventory")

    st.markdown("---")

    # ===========================
    # Pie Chart
    # ===========================

    st.subheader("📊 Inventory Status Distribution")

    status_counts = (
        inventory["Status"]
        .value_counts()
        .reset_index()
    )

    status_counts.columns = ["Status", "Count"]

    fig = px.pie(
        status_counts,
        names="Status",
        values="Count",
        title="Inventory Status"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.markdown("---")

    # ===========================
    # Download Button
    # ===========================

    csv = inventory.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇ Download Inventory Report",
        data=csv,
        file_name="inventory_report.csv",
        mime="text/csv"
    )