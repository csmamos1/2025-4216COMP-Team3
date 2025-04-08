import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
df = pd.read_csv("MET Office Weather Data.csv")  # Replace with your actual filename

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

# Define color and style options
colors = ['orange', 'blue', 'green', 'red', 'purple', 'brown', 'teal', 'gray', 'olive', 'pink', 'navy', 'coral', 'black', 'gold']
linestyles = ['-', '--']

# Plot data in 5-year intervals
for start_year in range(1950, 2021, 5):
    end_year = start_year + 4
    subset = df[(df['year'] >= start_year) & (df['year'] <= end_year)]
    plt.plot(subset['date'], subset['sun'], label=f'Sun {start_year}-{end_year}', linestyle='-', linewidth=1)
    plt.plot(subset['date'], subset['af'], label=f'Frost {start_year}-{end_year}', linestyle='--', linewidth=1)

plt.xlabel('Date')
plt.ylabel('Value')
plt.title('Sunshine and Air Frost (5-Year Intervals, 1950–2020)')
plt.legend(ncol=2)
plt.grid(True)
plt.tight_layout()
plt.show()
