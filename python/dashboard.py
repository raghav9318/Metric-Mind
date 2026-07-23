import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/Sales.csv")

# Create TotalPrice if not available
if "TotalPrice" not in df.columns:
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

# Monthly Sales
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)
monthly_sales = df.groupby("Month")["TotalPrice"].sum()

# Product Sales
product_sales = df.groupby("Product")["TotalPrice"].sum()

# Customer Sales
customer_sales = (
    df.groupby("CustomerID")["TotalPrice"]
      .sum()
      .sort_values(ascending=False)
      .head(5)
)

# Create Dashboard
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# 1 Monthly Sales
axs[0,0].plot(monthly_sales.index, monthly_sales.values, marker="o")
axs[0,0].set_title("Monthly Sales")

# 2 Product Sales
axs[0,1].bar(product_sales.index, product_sales.values)
axs[0,1].set_title("Sales by Product")
axs[0,1].tick_params(axis='x', rotation=45)

# 3 Top Customers
axs[1,0].bar(customer_sales.index.astype(str), customer_sales.values)
axs[1,0].set_title("Top Customers")
axs[1,0].tick_params(axis='x', rotation=45)

# 4 Product Share
axs[1,1].pie(
    product_sales.values,
    labels=product_sales.index,
    autopct="%1.1f%%"
)
axs[1,1].set_title("Product Share")

plt.tight_layout()

plt.savefig("dashboard/Sales_Dashboard.png")

plt.show()