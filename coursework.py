import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("MET Office Weather Data.csv")  # Replace with your actual filename

# Drop rows with missing values in 'af' or 'sun'
df = df.dropna(subset=['af', 'sun'])

# Create a datetime column for indexing
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

# Sort by date just in case
df = df.sort_values('date')

# Plot the line graph
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['sun'], label='Sunshine (hours)', color='orange')
plt.plot(df['date'], df['af'], label='Days of Air Frost', color='blue')

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Monthly Sunshine and Air Frost Trends')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
