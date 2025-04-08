import csv
import pandas as pd
import matplotlib.pyplot as plt


# Just put the file in the code 
file_path = r"C:\Users\Benson Lu\Desktop\First year Coursework\Second semester\Computer science workshop\csws-week1\MET Office Weather Data.csv"

# Loads the weather data CSV file into a pandas DataFrame called 'dv'
df = pd.read_csv(file_path)

# Filters the dataset to include only rows hwere the station name is "Aberrpoth"and will ignores other location 
aberporth_df = df[df['station'].str.lower().str.strip() == 'aberporth']

# Parse the date from year and month
aberporth_df['month_parsed'] = pd.to_datetime(
    aberporth_df['year'].astype(int).astype(str) + '-' + aberporth_df['month'].astype(int).astype(str),
    errors='coerce'
)

# Sorting Data by Date
aberporth_df = aberporth_df.sort_values('month_parsed')

# Get max and min rain imformation for the data
max_rain_row = aberporth_df.loc[aberporth_df['rain'].idxmax()]
min_rain_row = aberporth_df.loc[aberporth_df['rain'].idxmin()]

# Print max and min rainfall infomation for the data 
print("Max Rain:", max_rain_row['rain'], "mm")
print("Year:", max_rain_row['month_parsed'].year, "Month:", max_rain_row['month_parsed'].month)

print("Min Rain:", min_rain_row['rain'], "mm")
print("Year:", min_rain_row['month_parsed'].year, "Month:", min_rain_row['month_parsed'].month)

#This part is going to output the graph

# Plotting the rainfall
plt.figure(figsize=(12, 6))
plt.plot(aberporth_df['month_parsed'], aberporth_df['rain'], label='Monthly Rainfall (mm)', linewidth=1)

# Highlight max and min points
plt.scatter(max_rain_row['month_parsed'], max_rain_row['rain'], color='red', label='Max Rain')
plt.scatter(min_rain_row['month_parsed'], min_rain_row['rain'], color='blue', label='Min Rain')

# Add labels and title
plt.title("Monthly Rainfall in Aberporth")
plt.xlabel("Date")
plt.ylabel("Rainfall (mm)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show plot
plt.show()