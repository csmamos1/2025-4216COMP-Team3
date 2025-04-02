import pandas
import csv#rainfall and sun
rainfall = []
sun = []
with open('MET Office Weather Data.csv','r') as f:
    csv_reader = csv.reader(f)
    headers=next(csv_reader)
    rainfall_idx = headers.index('rain')
    sun_idx = headers.index('sun')
    
    for row in csv_reader:  # Handle NA values for rainfall
        rain_val = row[rainfall_idx]#done so it knows which row to follow for rain
        rainfall.append(float(rain_val) if rain_val != 'NA' else None)#makes sure na values are not shown
        
        # Handle NA values for sun
        sun_val = row[sun_idx]#done so it knows which row to follow for sun
        sun.append(float(sun_val) if sun_val != 'NA' else None)
        
valid_pairs = [(r, s) for r, s in zip(rainfall, sun) if r is not None and s is not None]
years_more_rain = sum(r > s for r, s in valid_pairs)
years_more_sun = sum(s > r for r,s in valid_pairs)
listlength = len(valid_pairs)
print(years_more_rain/listlength)
print(years_more_sun/listlength)
#print(f"Days with more rainfall than sun: {years_more_rain}")
#print(f"Days with more sun than rainfall: {years_more_sun}")
#print(f"Valid comparisons: {listlength} out of {len(rainfall)} total days")#shows how many valid days were used
