import pandas as pd

sales = pd.read_csv("data/salesdaily.csv")

# Convert date
sales["datum"] = pd.to_datetime(sales["datum"])

# Remove duplicates
sales = sales.drop_duplicates()

# Rename column
sales.rename(
    columns={"Weekday Name": "Weekday_Name"},
    inplace=True
)

# Missing values
print(sales.isnull().sum())

# Save cleaned file
sales.to_csv("data/clean_salesdaily.csv", index=False)

print("Data Cleaning Completed Successfully!")