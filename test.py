import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("aberporth_weather.csv")  # Replace with your actual filename

# Clean the data
df.replace("NA", pd.NA, inplace=True)
df.dropna(subset=["af", "sun"], inplace=True)

# Convert to appropriate data types
df["af"] = pd.to_numeric(df["af"])
df["sun"] = pd.to_numeric(df["sun"])

# Calculate the correlation
correlation = df["af"].corr(df["sun"])
print(f"Correlation between days of frost (af) and sunshine (sun): {correlation:.2f}")

# Visualize the relationship
plt.figure(figsize=(10, 6))
sns.regplot(x="sun", y="af", data=df)
plt.title("Correlation Between Days of Air Frost (af) and Sunshine (sun)")
plt.xlabel("Sunshine (hours)")
plt.ylabel("Days of Air Frost")
plt.grid(True)
plt.tight_layout()
plt.show()
