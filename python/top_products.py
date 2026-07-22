import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Sales.csv")

top_products = (
    df.groupby("Product")["TotalPrice"]
    .sum()
    .sort_values(ascending=False)
    .head(5)
)

print(top_products)

plt.figure(figsize=(8,5))
plt.bar(top_products.index, top_products.values)

plt.title("Top 5 Best Selling Products")
plt.xlabel("Product")
plt.ylabel("Total Sales")

plt.savefig("dashboard/Top_5_Products.png")

plt.show()