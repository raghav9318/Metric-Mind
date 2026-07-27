import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/Sales.csv")

# Count referral sources
referral_count = df["ReferralSource"].value_counts()

print(referral_count)

# Plot chart
plt.figure(figsize=(8,5))

plt.bar(referral_count.index, referral_count.values)

plt.title("Referral Source Analysis")
plt.xlabel("Referral Source")
plt.ylabel("Number of Customers")

plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("dashboard/Referral_Source_Analysis.png")

plt.show()