import pandas as pd

sales = pd.read_csv("data/salesdaily.csv")

print("===== First 5 Rows =====")
print(sales.head())

print("\n===== Last 5 Rows =====")
print(sales.tail())

print("\n===== Shape =====")
print(sales.shape)

print("\n===== Columns =====")
print(sales.columns)

print("\n===== Information =====")
print(sales.info())

print("\n===== Missing Values =====")
print(sales.isnull().sum())

print("\n===== Duplicate Rows =====")
print(sales.duplicated().sum())

print("\n===== Summary Statistics =====")
print(sales.describe())


# Load dataset
sales = pd.read_csv("data/salesdaily.csv")

# Check data types
print(sales.dtypes)

# Convert date column
sales["datum"] = pd.to_datetime(sales["datum"])

# Check missing values
print(sales.isnull().sum())

# Remove duplicate rows
sales = sales.drop_duplicates()

# Rename column
sales.rename(columns={"Weekday Name": "Weekday_Name"}, inplace=True)

# Save cleaned dataset
sales.to_csv("data/clean_salesdaily.csv", index=False)

print("Data Cleaning Completed Successfully!")

sales = pd.read_csv("data/salesdaily.csv")
print(sales.head())

medicine_sales = sales[['M01AB','M01AE','N02BA','N02BE','N05B','N05C','R03','R06']].sum()

print(medicine_sales)

medicine_sales.plot(kind='bar')

plt.title("Total Sales of Medicines")

plt.xlabel("Medicine")

plt.ylabel("Sales")

plt.show()

monthly_sales = sales.groupby("Month")[['M01AB','M01AE','N02BA','N02BE']].sum()

monthly_sales.plot(figsize=(10,6))

plt.title("Monthly Sales")

plt.show()

weekday_sales = sales.groupby("Weekday_Name")[['M01AB','M01AE','N02BA']].sum()

weekday_sales.plot(kind="bar")

plt.title("Weekday Sales")

plt.show()

sales = pd.read_csv("data/feature_engineered_sales.csv")

X = sales[[
    "Day",
    "Month",
    "Week",
    "Weekend",
    "M01AB_Lag1",
    "M01AB_MA7"
]]
y = sales["M01AB"]
X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.2,

    random_state=42
)
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

import pandas as pd
import numpy as np
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Load dataset
sales = pd.read_csv("data/feature_engineered_sales.csv")

# Features
X = sales[[
    "Day",
    "Month",
    "Week",
    "Weekend",
    "M01AB_Lag1",
    "M01AB_MA7"
]]

# Target
y = sales["M01AB"]

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = RandomForestRegressor(random_state=42)

# Train
model.fit(X_train, y_train)

# Predict
predictions = model.predict(X_test)

# Evaluate
mae = mean_absolute_error(y_test, predictions)
rmse = np.sqrt(mean_squared_error(y_test, predictions))
r2 = r2_score(y_test, predictions)

print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

# Compare
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

print(results.head())

# Save model
joblib.dump(model, "model.pkl")

model.fit(X_train, y_train)

joblib.dump(model, "model.pkl")


future_data = pd.DataFrame({
    "Day": [1],
    "Month": [7],
    "Week": [27],
    "Weekend": [0],
    "M01AB_Lag1": [11],
    "M01AB_MA7": [10.5]
})
import matplotlib.pyplot as plt

medicine_sales.plot(kind="bar")

plt.title("Total Medicine Sales")
plt.xlabel("Medicine")
plt.ylabel("Sales")

plt.show()