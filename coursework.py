import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


def Abdulla():

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



data=pd.read_csv('MET Office Weather Data.csv')


def joseph():

# I excluded the year 1965 bcause there was missing data values!
    new_data_Hurn = data[data["rain"].notna() & (data["station"]=="hurn") & 
                    (data["tmin"].notna())& (data["year"]!="1965.0")]
                

    pd.set_option("display.max_rows", None)  # force python to display all rows and columns
    pd.set_option("display.max_columns", None)  

    #print(new_data)


#although indices where present was getting empty column, problem could be after deleted rows so reconfigured indices
    new_data0 = new_data_Hurn.reset_index(drop=True)

    new_data1= new_data0[(new_data0["year"]<2020.0)]

    year_counts = new_data1["year"].value_counts()
    year_range = range(1957, 2020)  
    year_counts = year_counts.reindex(year_range, fill_value=0)
   
    tmin_range=new_data1["tmin"]       
    tmin_averages=[]
    for start in range(0, 753, 12):
        end = start + 12
        tmin_averages.append(tmin_range[start:end].sum()/12)  # values are summed from starrt to end and than /12 to get the averages
    

    rain_range=new_data1["rain"]
    rain_averages=[]
    for start in range (0,753,12):
        end = start +12
        rain_averages.append(rain_range[start:end].sum()/12)

    std_dev_rain=np.std(rain_averages)
    std_dev_tmin= np.std(tmin_averages)
    mean_tmin_averages= np.mean(tmin_averages)
    mean_rain_averages=np.mean(rain_averages)
    CV_rain= (std_dev_rain/mean_rain_averages)*100
    CV_tmin= (std_dev_tmin/mean_tmin_averages)*100 
    total_months = 64 * 12  # Expected months
    missing_months = 3
    observed_months = total_months - missing_months
    missing_percentage = (missing_months / total_months) * 100

    print(f"\n The average minimum temperature from the years 1957-2019 in Hurn is \n  "
          f"{mean_tmin_averages:.2f} celcius and the standard deviation"
           f" (that is how much the the data deviates from the mean)\n"
            f" is {std_dev_tmin:.2f} celsius thus each point of data deviates from the mean(Minimum teperature between 1957-2019)" 
            f" by about {CV_tmin:.2f}% \n"
            f" which is a very negligible and shows a tight consistency between the data points \n"
            f" addiditonally there is a {missing_percentage:.2f}% error of the new data relative to the original")
    
    print(f"\n The average amount of rainfall from the years 1957-2019 in Hurn is \n  "
          f"{mean_rain_averages:.2f}mm and the standard deviation"
           f" (that is how much the the data deviates from the mean)\n"
            f" is {std_dev_rain:.2f}mm  thus each point of data deviates from the mean(Minimum teperature between 1957-2019)"
             f" by about {CV_rain:.2f}% \n "
            f" which is a moderate value and shows that the data points a relatively consistent with"
             f" the overall average. \n addiditonally there is a {missing_percentage:.2f}%"
             f"error of the new data relative to the original")
    
    
    range_years= list(range(1957,2020))
    ###print(range_years)





    fig, ax = plt.subplots()
    ax.plot( range_years, tmin_averages,'mD', label="tmin_averages")
    fig.suptitle("Average Minimum Temerature per year", fontsize=20)
    ax.set_title("Station: Hurn", fontsize=14)
    ax.set_xlabel("Years from 1957-2019", fontsize=12, color='r')
    ax.set_ylabel("Average Minimum temperature per year",fontsize=12, color='r')
    ax.xaxis.grid()
    ax.yaxis.grid()
    ax.set_yticks(range(3,10,1))

    ax.set_xticks(range(1957,2020,1)) 
    ax.set_xticklabels(range_years, fontsize=8, rotation=45)
    z=np.arange(1957, 2021)
    ax.set_xlim(z.min()-1, z.max())
    mean_val = np.mean(tmin_averages)
    plt.axhline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
    ax.legend()

    

    plt.show()
    

    #####******PAY ATTENTION NEED TO FIND MIN AND MAX VALUES FOR RAIN SO I CAN KNOW LIMITS FOR GRAPH****#######
    fig, ax = plt.subplots()
    ax.plot( range_years, rain_averages, 'mD',  label= "rain averages")
    fig.suptitle("Average Rainfall from per year", fontsize=20)
    ax.set_title("Station: Hurn", fontsize=14)
    ax.set_xlabel("Years from 1957-2019", fontsize=12, color='r')
    ax.set_ylabel("Average rainfall per mm",fontsize=12, color='r')

    ax.xaxis.grid()
    ax.yaxis.grid()
    ax.set_yticks(range(30,120,5))

    ax.set_xticks(range(1957,2020,1)) 

    x=np.arange(1957, 2021)
    ax.set_xticklabels(range_years, fontsize=8)
    ax.set_xticklabels(range_years, fontsize=8, rotation=45)  # Adjust font size here
    ax.set_yticklabels(ax.get_yticks(), fontsize=8)
    ax.set_xlim(x.min()-1, x.max())  # Ensures no extra padding at the edges
    mean_val = np.mean(rain_averages)
    plt.axhline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
    ax.legend()
    plt.show()



    fig, ax = plt.subplots()
    fig.suptitle("Minimum average temperature \n against average rainfall against year", fontsize=18)
    ax.plot(range_years, tmin_averages, 'mD:')
    ax.set_ylabel("Average Minimum temperature", color='m')
    ax1 = ax.twinx()
    ax1.plot(range_years, rain_averages, 'ro--')
    ax1.set_ylabel("Average rainfall", color='r')
    
    plt.show()



    #print(f"{min(rain_averages):.2f}")  
    #print(f"{max(rain_averages):.2f}")






def Jake():
    
    df = pd.read_csv("MET Office Weather Data.csv")
    
    df = df.dropna(subset=['sun', 'month'])
    
    # Daytime column
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))
    
    # Data between 1970 and 2020 only
    df = df[(df['year'] >= 1970) & (df['year'] <= 2020)]
    
    # Sort by date
    df = df.sort_values('date')
    
    # Calculate monthly averages
    monthly_avg = df.groupby('month')['sun'].mean()
    
    # Create plot
    plt.figure(figsize=(14, 7))
    
    # Bar chart of monthly averages
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    plt.bar(months, monthly_avg, color='orange', alpha=0.7, label='Avg Sunshine Hours')
    
    # Customize the plot
    plt.xlabel('Month')
    plt.ylabel('Sunshine Hours')
    plt.title('Average Monthly Sunshine (1970–2020)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    
    # Add value labels on bars
    for i, value in enumerate(monthly_avg):
        plt.text(i, value + 5, f"{value:.1f}", ha='center')
    
    plt.tight_layout()
    plt.show()


def Benson():

            # Just put the file in the code 
        file_path = r"MET Office Weather Data.csv"

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
        
def Peter():
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

def Muhammad():
    # Load the CSV file 
    file_path = "MET Office Weather Data.csv"
    df = pd.read_csv(file_path)

    # Filter for 'aberporth' station
    df_aberporth = df[df["station"] == "aberporth"]

    # Drop rows with missing tmax or tmin values
    df_aberporth = df_aberporth.dropna(subset=["tmax", "tmin"])

    # Convert year and month into a datetime format for better plotting
    df_aberporth["date"] = pd.to_datetime(df_aberporth[["year", "month"]].assign(day=1))

    # Sort by date
    df_aberporth = df_aberporth.sort_values("date")

    # Plot temperature trends
    plt.figure(figsize=(12, 6))
    plt.plot(df_aberporth["date"], df_aberporth["tmax"], label="Max Temperature (°C)", color="red")
    plt.plot(df_aberporth["date"], df_aberporth["tmin"], label="Min Temperature (°C)", color="blue")

    # Formatting the plot
    plt.xlabel("Year")
    plt.ylabel("Temperature (°C)")
    plt.title("Aberporth Minimum and Maximum Temperatures Over Time")
    plt.legend()
    plt.grid(True)
    plt.show()




    

while True:
    Visualisation = input("\n Please type \033[1mJoseph()\033[0m to see average minimum temperature against years(1957-2019) visualization, " \
    "\n aaverage rainfall against years(1957-2019) "
    "visualization and average \n minimum temperature againt rainfall against years(1957-2019) for the Station 'Hurn' visualisation \n"
    "\ntype \033[1mAbdulla()\033[0m if you wish to air frost and sun\n"
    "\ntype \033[1mJake()\033[0m if you wish to average hours of sunlight against months\n"
    "\ntype \033[1mBenson()\033[0m if you wish to see rainfall against months data \n"
    "\ntype \033[1mPeter()\033[0m if you wish to see the correlation between sunshine and rain\n"
    "\ntype \033[1mMuhammad()\033[0m Minimum and Maximum temperature for aberpoth \n")
    if Visualisation == 'quit':
        break

    if Visualisation.lower() == "joseph()":
        joseph()

    if Visualisation.lower()=="abdulla()":

        Abdulla()

    if Visualisation.lower()=="jake()":

        Jake()   

    if Visualisation.lower()=="benson()":   
        
        Benson()
        
    if Visualisation.lower()=="peter()":   
        
        Peter()
    if Visualisation.lower()=="muhammad()": 

        Muhammad()   

    else:
        print("There is no data matching this imput") 
        
        