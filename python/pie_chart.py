import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Sales.csv")

sales = df.groupby("Product")["TotalPrice"].sum()

plt.figure(figsize=(8,8))

plt.pie(
    sales.values,
    labels=sales.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Sales Distribution by Product")

plt.savefig("dashboard/Sales_Pie_Chart.png")

plt.show()