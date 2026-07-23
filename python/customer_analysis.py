import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/Sales.csv")

# Customer-wise total sales
customer_sales = df.groupby("CustomerID")["TotalPrice"].sum()

# Top 10 customers
top_customers = customer_sales.sort_values(ascending=False).head(10)

print(top_customers)

# Plot
plt.figure(figsize=(10,5))
plt.bar(top_customers.index.astype(str), top_customers.values)

plt.title("Top 10 Customers by Total Sales")
plt.xlabel("Customer ID")
plt.ylabel("Total Sales")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("dashboard/Top_Customers.png")

plt.show()