import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Sales.csv")

df["Date"] = pd.to_datetime(df["Date"])

monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["TotalPrice"].sum()

monthly_sales.index = monthly_sales.index.astype(str)

plt.figure(figsize=(10,5))

plt.plot(
    monthly_sales.index,
    monthly_sales.values,
    marker="o"
)

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid(True)

plt.savefig("dashboard/Monthly_Sales_Trend.png")

plt.show()