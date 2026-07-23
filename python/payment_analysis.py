import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/Sales.csv")

# Create TotalPrice if missing
if "TotalPrice" not in df.columns:
    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

payment_sales = df.groupby("PaymentMethod")["TotalPrice"].sum().sort_values()

print(payment_sales)

plt.figure(figsize=(8,5))
plt.bar(payment_sales.index, payment_sales.values)

plt.title("Sales by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Total Sales")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("dashboard/Payment_Method_Sales.png")

plt.show()