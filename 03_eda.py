import pandas as pd
import matplotlib.pyplot as plt

sales = pd.read_csv("data/clean_salesdaily.csv")

medicine_sales = sales[
    ["M01AB","M01AE","N02BA","N02BE","N05B","N05C","R03","R06"]
].sum()

print(medicine_sales)

medicine_sales.plot(kind="bar", figsize=(10,6))

plt.title("Total Medicine Sales")
plt.xlabel("Medicine")
plt.ylabel("Total Sales")
plt.grid(True)

plt.show()

monthly_sales = sales.groupby("Month")[
    ["M01AB","M01AE","N02BA","N02BE"]
].sum()

monthly_sales.plot(figsize=(10,6))

plt.title("Monthly Sales")

plt.show()

weekday_sales = sales.groupby("Weekday_Name")[
    ["M01AB","M01AE","N02BA"]
].sum()

weekday_sales.plot(kind="bar")

plt.title("Weekday Sales")

plt.show()