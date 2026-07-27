import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Sales.csv")

# Count coupon usage
coupon_count = df["CouponCode"].value_counts()

print(coupon_count)

# Plot graph
plt.figure(figsize=(8,5))

plt.bar(coupon_count.index, coupon_count.values)

plt.title("Coupon Code Usage")
plt.xlabel("Coupon Code")
plt.ylabel("Number of Orders")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig("dashboard/Coupon_Analysis.png")

plt.show()