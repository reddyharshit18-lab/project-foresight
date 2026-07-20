import pandas as pd

sales = pd.read_csv("data/clean_salesdaily.csv")

sales["datum"] = pd.to_datetime(sales["datum"])

sales["Day"] = sales["datum"].dt.day

sales["Week"] = sales["datum"].dt.isocalendar().week

sales["Weekend"] = sales["datum"].dt.dayofweek

sales["Weekend"] = sales["Weekend"].apply(
    lambda x: 1 if x >= 5 else 0
)

sales["M01AB_Lag1"] = sales["M01AB"].shift(1)

sales["M01AB_MA7"] = sales["M01AB"].rolling(7).mean()

sales.fillna(0, inplace=True)

sales.to_csv(
    "data/feature_engineered_sales.csv",
    index=False
)

print("Feature Engineering Completed!")