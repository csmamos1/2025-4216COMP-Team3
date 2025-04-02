import matplotlib.pyplot as plt
import csv

sun = []
month = []
year = [] 

with open('MET Office Weather Data.csv', 'r') as f:
    csv_reader = csv.reader(f)
    headers = next(csv_reader)
    
    try:
        sun_idx = headers.index('sun')
        month_idx = headers.index('month')
        year_idx = headers.index('year')  
    except ValueError as e:
        print(f"Column not found in headers: {e}")
        exit()

    for row in csv_reader:
        try:
            #sun values
            sun_val = row[sun_idx]
            sun.append(float(sun_val) if sun_val != 'NA' else None)
            
            #month values
            month_val = row[month_idx]
            month.append(int(float(month_val)) if month_val != 'NA' else None)  # Convert to int
            
            #year values
            year_val = row[year_idx]
            year.append(int(float(year_val)) if year_val != 'NA' else None)
        except (ValueError, IndexError) as e:
            print(f"Skipping row due to error: {e}")
            sun.append(None)
            month.append(None)
            year.append(None)
            continue


valid_pairs = [(s, m, y) for s, m, y in zip(sun, month, year) 
              if s is not None and m is not None and y is not None 
              and 1970 <= y <= 2020]

filtered_sun = [s for s, m, y in valid_pairs]
filtered_month = [m for s, m, y in valid_pairs]

months_more_sun = sum(s > m * 30 for s, m, y in valid_pairs)
total_comparisons = len(valid_pairs)
average_sun = sum(filtered_sun) / total_comparisons if total_comparisons > 0 else 0

print(f"Months with more than 30h/day equivalent sunshine: {months_more_sun}")
print(f"Valid comparisons: {total_comparisons}")
print(f"Average sunshine hours: {average_sun:.2f}")


plt.figure(figsize=(12, 6))

#month plots
month_names = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_avg = [0] * 12
monthly_counts = [0] * 12

for s, m, y in valid_pairs:
    monthly_avg[m-1] += s
    monthly_counts[m-1] += 1

monthly_avg = [total/count if count > 0 else 0 for total, count in zip(monthly_avg, monthly_counts)]

#bar chart
bars = plt.bar(range(1, 13), monthly_avg, color='orange', alpha=0.7)

#labels
plt.title('Average Monthly Sunshine Hours (1970-2020)', fontsize=14)
plt.xlabel('Month', fontsize=12)
plt.ylabel('Sunshine Hours', fontsize=12)
plt.xticks(range(1, 13), month_names)
plt.grid(axis='y', linestyle='--', alpha=0.5)

for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}', ha='center', va='bottom')

plt.tight_layout()
plt.show()
