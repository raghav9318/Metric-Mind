import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Sales.csv")

# Count each order status
status_count = df["OrderStatus"].value_counts()

print(status_count)

# Plot chart
plt.figure(figsize=(8,5))

plt.bar(status_count.index, status_count.values)

plt.title("Order Status Analysis")
plt.xlabel("Order Status")
plt.ylabel("Number of Orders")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("dashboard/Order_Status_Analysis.png")

plt.show()
