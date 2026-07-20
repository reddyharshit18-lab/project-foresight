import pandas as pd

inventory = pd.DataFrame({
    "Medicine": ["M01AB", "M01AE", "N02BA"],
    "Current_Stock": [20, 120, 50],
    "Forecast": [35, 30, 45]
})

def check_risk(stock, forecast):

    if stock < forecast:
        return "Stockout Risk"

    elif stock > forecast * 3:
        return "Overstock"

    else:
        return "Healthy"

inventory["Status"] = inventory.apply(
    lambda row: check_risk(
        row["Current_Stock"],
        row["Forecast"]
    ),
    axis=1
)

def recommendation(status):

    if status == "Stockout Risk":
        return "Reorder"

    elif status == "Overstock":
        return "Discount"

    else:
        return "No Action"

inventory["Recommendation"] = inventory["Status"].apply(recommendation)

print(inventory)

inventory.to_csv("data/inventory_report.csv", index=False)