import pandas
import matplotlib.pyplot as plt
import csv#rainfall and sun
rainfall = []
sun = []
with open('MET Office Weather Data.csv','r') as f:
    csv_reader = csv.reader(f)
    headers=next(csv_reader)
    rainfall_idx = headers.index('rain')
    sun_idx = headers.index('sun')
    
    for row in csv_reader:  # Handle NA values for rainfall
        rain_val = row[rainfall_idx]
        rainfall.append(float(rain_val) if rain_val != 'NA' else None)
        
        # Handle NA values for sun
        sun_val = row[sun_idx]
        sun.append(float(sun_val) if sun_val != 'NA' else None)
        
valid_pairs = [(r, s) for r, s in zip(rainfall, sun) if r is not None and s is not None]
days_more_rain = sum(r > s for r, s in valid_pairs)

print(f"Days with more rainfall than sun: {days_more_rain}")
print(f"Valid comparisons: {len(valid_pairs)} out of {len(rainfall)} total days")

    
