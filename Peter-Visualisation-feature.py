rainfall = []
sun = []
with open('MET Office Weather Data.csv','r') as f:#Opens csv file
    csv_reader = csv.reader(f)#allows for data to be read
    headers=next(csv_reader)
    rainfall_idx = headers.index('rain')
    sun_idx = headers.index('sun')
   
    for row in csv_reader:  #For NA values 
        rain_val = row[rainfall_idx]#done so it knows which row to follow for rain
        rainfall.append(float(rain_val) if rain_val != 'NA' else None)#makes sure na values are not shown
        
        
        sun_val = row[sun_idx]#done so it knows which row to follow for sun
        sun.append(float(sun_val) if sun_val != 'NA' else None)
        

        
valid_pairs = [(r, s) for r, s in zip(rainfall, sun) if r is not None and s is not None]#only allows valid pairs to be shown in grap
rain_valid = [pair[0] for pair in valid_pairs]
sun_valid = [pair[1] for pair in valid_pairs]

plt.subplot(2, 1, 2)#plots the graph
scatter = plt.scatter(rain_valid, sun_valid, c=range(len(rain_valid)), 
                     cmap='viridis', alpha=0.7, s=100, edgecolor='w')


plt.title('Rainfall vs Sunshine Correlation', pad=10, fontsize=14)#adds the labels to the graph
plt.xlabel('Rainfall (mm)', fontsize=12)
plt.ylabel('Sunshine (hours)', fontsize=12)

plt.tight_layout()
plt.show()
