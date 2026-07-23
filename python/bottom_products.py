import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/Sales.csv")

# Product-wise total sales
sales = df.groupby("Product")["TotalPrice"].sum()

# Bottom 5 products
bottom = sales.sort_values().head(5)

print(bottom)

# Plot
plt.figure(figsize=(8,5))
plt.barh(bottom.index, bottom.values)

plt.title("Bottom 5 Selling Products")
plt.xlabel("Total Sales")
plt.ylabel("Product")

plt.tight_layout()

plt.savefig("dashboard/Bottom_5_Products.png")

plt.show()