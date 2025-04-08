import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("MET Office Weather Data.csv")

# Drop rows with missing values in 'af' or 'sun'
df = df.dropna(subset=['af', 'sun'])

# Create a datetime column for indexing
df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

# Filter data between 1950 and 2020
df = df[(df['year'] >= 1950) & (df['year'] <= 2020)]

# Sort by date
df = df.sort_values('date')

# Create plot
plt.figure(figsize=(14, 7))

# Plot sunshine data in orange
plt.plot(df['date'], df['sun'], label='Sunshine (hours)', color='orange', linestyle='-')

# Plot air frost data in blue
plt.plot(df['date'], df['af'], label='Days of Air Frost', color='blue', linestyle='--')

# Customize the plot
plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Sunshine and Air Frost Trends (1950–2020)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
