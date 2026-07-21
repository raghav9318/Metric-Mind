import pandas as pd
import matplotlib.pyplot as plt
df= pd.read_csv("data/Sales.csv")
sales = df.groupby("Product")["TotalPrice"].sum()
print(sales)
plt.figure(figsize=(8,5))
plt.bar(sales.index,sales.values)
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.savefig("dashboard/Total_Sales_By_Product.png")
plt.show()
