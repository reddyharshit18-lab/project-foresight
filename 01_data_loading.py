import pandas as pd

# Load Dataset
sales = pd.read_csv("data/salesdaily.csv")

print("="*50)
print("First 5 Rows")
print(sales.head())

print("="*50)
print("Last 5 Rows")
print(sales.tail())

print("="*50)
print("Shape")
print(sales.shape)

print("="*50)
print("Columns")
print(sales.columns)

print("="*50)
print("Information")
print(sales.info())

print("="*50)
print("Missing Values")
print(sales.isnull().sum())

print("="*50)
print("Duplicate Rows")
print(sales.duplicated().sum())

print("="*50)
print("Summary Statistics")
print(sales.describe())