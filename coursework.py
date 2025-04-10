import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv


def Abdulla():

   def Abdulla():
    # Load the CSV file
    df = pd.read_csv("MET Office Weather Data.csv")

    # Drop rows with missing values in 'af' or 'sun'
    df = df.dropna(subset=['af', 'sun'])

    # Create a datetime column for indexing
    df['date'] = pd.to_datetime(df[['year', 'month']].assign(day=1))

    # Filter data between 2000 and 2020
    df = df[(df['year'] >= 2000) & (df['year'] <= 2020)]

    # Sort by date
    df = df.sort_values('date')

    # Separate data by location
    aberporth = df[df['station'].str.lower() == 'aberporth']
    ballypatrick = df[df['station'].str.lower() == 'ballypatrick']

    # Create plot
    plt.figure(figsize=(14, 7))

    # Plot sunshine data
    plt.plot(aberporth['date'], aberporth['sun'], label='Sunshine - Aberporth', color='orange')
    plt.plot(ballypatrick['date'], ballypatrick['sun'], label='Sunshine - Ballypatrick', color='red')

    # Plot air frost data
    plt.plot(aberporth['date'], aberporth['af'], label='Air Frost - Aberporth', linestyle='--', color='blue')
    plt.plot(ballypatrick['date'], ballypatrick['af'], label='Air Frost - Ballypatrick', linestyle='--', color='green')

    # Customize the plot
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.title('Sunshine and Air Frost Trends (2000–2020)')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()



data=pd.read_csv('MET Office Weather Data.csv')


def Joseph():



    #exlcude 2020 as there are missing data values
    new_data_Hurn = data[data["rain"].notna() & (data["station"]=="hurn") & 
                    (data["tmin"].notna())& (data["year"]<2020)]
                
    #print (len(new_data_Hurn))

    pd.set_option("display.max_rows", None)  # Show all rows
    pd.set_option("display.max_columns", None)  # Show all columns

    #print(new_data)


    #although indices where present was getting empty column,
    #problem could be after deleted rows so reconfigured indices
    new_data0 = new_data_Hurn.reset_index(drop=True)


    #print(len(new_data0)) # want to find how many months in total in my data set
    #after finding there 753months 753/12 gives float, means some years must have less months

    year_counts = new_data0["year"].value_counts()
    year_range = range(1957, 2020)  
    year_counts = year_counts.reindex(year_range, fill_value=0)
    #print(year_counts)
    # so i counted how many months each year had and found that 2009,2015,2016 all have 11months
    #this makes sense because (63*12=756)-3 = 753, there are three months missing so i forced pandas to show all
    #the whole data set and founf that febuary is missing in each case, i want to include this analysis to show
    #a margin of error.
    #total_months = 64 * 12  # Expected months
    #missing_months = 3
    #observed_months = total_months - missing_months
    #missing_percentage = (missing_months / total_months) * 100
    #print(f"Missing Data Percentage: {missing_percentage:.2f}%")

    new_data_Bradford = data[data["rain"].notna() & (data["station"]=="bradford") & 
                    (data["tmin"].notna())& (data["year"]>1956)& (data["year"] <2020.0)]
    


    #print(len(new_data_Bradford))

    pd.set_option("display.max_rows", None)  # Show all rows
    pd.set_option("display.max_columns", None)  # Show all columns

    new_datax = new_data_Bradford.reset_index(drop=True)
    
    year_counts = new_datax["year"].value_counts()
    year_rangex = range(1957, 2020)  
    year_counts = year_counts.reindex(year_rangex, fill_value=0)
    #print(year_counts)

    # calculate yearly tmin averages for station Hurn
    tmin_range=new_data0["tmin"]       
    tmin_averages=[]
    for start in range(0, 753, 12):
        end = start + 12
        tmin_averages.append(tmin_range[start:end].sum()/12)  # values are summed from starrt to end and than /12 to get the averages
    
    #calculate yearly rainfall averages for station Hurn
    rain_range=new_data0["rain"]
    rain_averages=[]
    for start in range (0,753,12):
        end = start +12
        rain_averages.append(rain_range[start:end].sum()/12)

    #calculate sd for rain and tmin yearly averages
    std_dev_rain=np.std(rain_averages)
    std_dev_tmin= np.std(tmin_averages)
    #calculate mean for averages accross 1957-2019 period
    mean_tmin_averages= np.mean(tmin_averages)
    mean_rain_averages=np.mean(rain_averages)
    # show the percentage of sd as coefficient variable
    CV_rain= (std_dev_rain/mean_rain_averages)*100
    CV_tmin= (std_dev_tmin/mean_tmin_averages)*100 
    #calculate percentage error
    total_months = 64 * 12  # Expected months
    missing_months = 3
    observed_months = total_months - missing_months
    missing_percentage = (missing_months / total_months) * 100

    #print(CV_rain)

    tmin_range1=new_datax["tmin"]       
    tmin_averages1=[]
    for start in range(0, 748, 12):
        end = start + 12
        tmin_averages1.append(tmin_range1[start:end].sum()/12)  
    #values are summed from starrt to end and than /12 to get the averages

    #calculate yearly rainfall for bradfor
    rain_range1=new_datax["rain"]
    rain_averages1=[]
    for start in range (0,748,12):
        end = start +12
        rain_averages1.append(rain_range1[start:end].sum()/12)
    #calculate, SD, CV, Mean an percentage error for bradford
    std_dev_rain1=np.std(rain_averages1)
    std_dev_tmin1= np.std(tmin_averages1)
    mean_tmin_averages1= np.mean(tmin_averages1)
    mean_rain_averages1=np.mean(rain_averages1)
    CV_rain1= (std_dev_rain1/mean_rain_averages1)*100
    CV_tmin1= (std_dev_tmin1/mean_tmin_averages1)*100 
    total_months1 = 64 * 12  # Expected months
    missing_months1 = 3
    observed_months1 = total_months1 - missing_months1
    missing_percentage1 = (missing_months1 / total_months1) * 100

    #print(CV_rain1)

    #plot for Hurn: min temp
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
    ax.set_xticks(range(1957,2020,1)) 
    ax.set_xticklabels(range_years, fontsize=8, rotation=45)
    trend=np.polyfit(range_years, tmin_averages, 1) 
    trend_line = np.poly1d(trend)(range_years)
    z=np.arange(1957, 2021)
    ax.set_xlim(z.min()-1, z.max())
    mean_val = np.mean(tmin_averages)
    ax.axhline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
    ax.plot(range_years, trend_line, color="orange", label="Trend Line")  

    ax.legend()

    

    plt.show()
    

    #plot for hurn: rainfall
    fig, ax = plt.subplots()
    ax.plot( range_years, rain_averages, 'mD',  label= "rain averages")
    fig.suptitle("Average Rainfall from per year", fontsize=20)
    ax.set_title("Station: Hurn", fontsize=14)
    ax.set_xlabel("Years from 1957-2019", fontsize=12, color='r')
    ax.set_ylabel("Average rainfall per mm",fontsize=12, color='r')

    ax.xaxis.grid()
    ax.yaxis.grid()
    ax.set_xticks(range(1957,2020,1)) 
    x=np.arange(1957, 2021)
    ax.set_xticklabels(range_years, fontsize=8, rotation=45)  # Adjust fontsize and rotation
    trend=np.polyfit(range_years, rain_averages, 1) 
    trend_line = np.poly1d(trend)(range_years)
    ax.set_xlim(x.min()-1, x.max())  # delete extra space at the end of grid
    mean_val = np.mean(rain_averages)
    plt.axhline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
    ax.plot(range_years, trend_line, color="orange", label="Trend Line")  
    ax.legend()
    
   


    plt.show()



    #plot for bradford: min temp
    range_years= list(range(1957,2020))
    fig, ax = plt.subplots()
    ax.plot( range_years, tmin_averages1,'mD', label="tmin_averages")
    fig.suptitle("Average Minimum Temerature per year", fontsize=20)
    ax.set_title("Station: Bradford", fontsize=14)
    ax.set_xlabel("Years from 1957-2019", fontsize=12, color='r')
    ax.set_ylabel("Average Minimum temperature per year",fontsize=12, color='r')
    ax.xaxis.grid()
    ax.yaxis.grid()
    ax.set_xticks(range(1957,2020,1)) 
    ax.set_xticklabels(range_years, fontsize=8, rotation=45)
    trend=np.polyfit(range_years, tmin_averages1, 1) 
    trend_line = np.poly1d(trend)(range_years)
    z=np.arange(1957, 2021)
    ax.set_xlim(z.min()-1, z.max())
    mean_val = np.mean(tmin_averages1)
    ax.axhline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
    ax.plot(range_years, trend_line, color="orange", label="Trend Line")  

    ax.legend()

    

    plt.show()

    #plot for bradford: rainfall 
    fig, ax = plt.subplots()
    ax.plot( range_years, rain_averages1, 'mD',  label= "rain averages")
    fig.suptitle("Average Rainfall from per year", fontsize=20)
    ax.set_title("Station: Bradford", fontsize=14)
    ax.set_xlabel("Years from 1957-2019", fontsize=12, color='r')
    ax.set_ylabel("Average rainfall per mm",fontsize=12, color='r')

    ax.xaxis.grid()
    ax.yaxis.grid()
    ax.set_xticks(range(1957,2020,1)) 
    x=np.arange(1957, 2021)
    ax.set_xticklabels(range_years, fontsize=8, rotation=45)  # Adjust fontsize and rotation
    trend=np.polyfit(range_years, rain_averages1, 1) 
    trend_line = np.poly1d(trend)(range_years)
    ax.set_xlim(x.min()-1, x.max())  # delete extra space at the end of grid
    mean_val = np.mean(rain_averages1)
    plt.axhline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
    ax.plot(range_years, trend_line, color="orange", label="Trend Line")  
    
    ax.legend()
    
   


    plt.show()



    #compare hurn and bradford min temp trend
    fig, ax = plt.subplots()
    fig.suptitle("Average Minimum Temperature ", fontsize=20)
    ax.set_title("Hurn Trend against Bradford Trend", fontsize=14)
    ax.set_ylabel("Average Minimum temperature", color='m')
    trend1=np.polyfit(range_years, tmin_averages, 1) 
    trend_line = np.poly1d(trend1)(range_years)
    ax.plot(range_years, trend_line, color="orange", label="Trend Line")
    ax1 = ax.twinx()
    ax1.set_ylabel("Average minimum temperature", color='r')
    trend2=np.polyfit(range_years, tmin_averages1, 1) 
    trend_line1 = np.poly1d(trend2)(range_years)
    ax1.plot(range_years, trend_line1, color="blue", label="Trend Line")  
    ax.legend()
    ax1.legend()
    plt.show()

    #compare for hurn & bradford: rainfall trend
    fig, ax = plt.subplots()
    fig.suptitle("Average Rainfall ", fontsize=20)
    ax.set_title("Hurn Trend against Bradford Trend", fontsize=14)
    ax.set_ylabel("Average rainfall in Hurn", color='orange')
    trend1=np.polyfit(range_years, rain_averages, 1) 
    trend_line1 = np.poly1d(trend1)(range_years)
    ax.plot(range_years, trend_line1, color="orange", label="Hurn Trend Line")
    ax1 = ax.twinx()
    ax1.set_ylabel("Average rainfall in Bradford", color='blue')
    trend2=np.polyfit(range_years, rain_averages1, 1) 
    trend_line2 = np.poly1d(trend2)(range_years)
    ax1.plot(range_years, trend_line2, color="blue", label=" Bradford Trend Line")  
    ax.legend()
    ax1.legend()
    plt.show()



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

    # Load the weather data  CSV file into a pandas DataFrame called 'df'
    df = pd.read_csv("MET Office Weather Data.csv")

    # Filter for the two stations is "Aberrpoth" and "Armagh"
    stations = ["aberporth", "armagh"]
    df_filtered = df[df["station"].isin(stations)].dropna(subset=["rain"])

    # === RAINFALL REPORT ===
    print("=== Rainfall Report Per Station ===")
    for station in stations:
        station_data = df_filtered[df_filtered["station"] == station]
        #Get Max and Min rainfall information 
        max_row = station_data.loc[station_data["rain"].idxmax()]
        min_row = station_data.loc[station_data["rain"].idxmin()]
        #Print Maximum rainfall information 
        #Print year and month information 
        print(f"\n>> Max Rainfall - {station.title()}:")
        print(f"Year: {int(max_row['year'])}, Month: {int(max_row['month'])}, Rainfall: {max_row['rain']} mm")
        #Print Mainmum rainfall information 
        #Print year and month information
        print(f">> Min Rainfall - {station.title()}:")
        print(f"Year: {int(min_row['year'])}, Month: {int(min_row['month'])}, Rainfall: {min_row['rain']} mm")

    # === PLOT SCATTER CHART ===
    plt.figure(figsize=(14, 6))

    # Color settings
    main_colors = {"aberporth": "blue", "armagh": "green"}
    highlight_colors = {
    "aberporth": {"max": "red", "min": "orange"},
    "armagh": {"max": "purple", "min": "gold"}
    }

    for station in stations:
        station_data = df_filtered[df_filtered["station"] == station].copy()
        station_data["date"] = pd.to_datetime(station_data[["year", "month"]].assign(day=1))

    # Plot all rainfall points
        plt.scatter(
            station_data["date"],
            station_data["rain"],
            color=main_colors[station],
            label=f"{station.title()} Data",
            s=10
    )

        # Max Rainfall
        max_row = station_data.loc[station_data["rain"].idxmax()]
        plt.scatter(max_row["date"], max_row["rain"],
                color=highlight_colors[station]["max"],
                s=80, label=f"Max - {station.title()}")
        plt.text(max_row["date"], max_row["rain"] + 5,
             f"{int(max_row['year'])}-{int(max_row['month'])}",
             color=highlight_colors[station]["max"])

        # Min Rainfall
        min_row = station_data.loc[station_data["rain"].idxmin()]
        plt.scatter(min_row["date"], min_row["rain"],
                color=highlight_colors[station]["min"],
                s=80, label=f"Min - {station.title()}")
        plt.text(min_row["date"], min_row["rain"] + 5,
             f"{int(min_row['year'])}-{int(min_row['month'])}",
             color=highlight_colors[station]["min"])

    # Final plot styling
    plt.title("Rainfall in Aberporth and Armagh - Max and Min Highlighted")
    plt.xlabel("Year")
    plt.ylabel("Rainfall (mm)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    #Show plot
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
    Visualisation = input("\n Please type \033[1mJoseph()\033[0m to see average min temp and rainfall against years(1957-2019) visualization for hurn, " 
    "and the average min temp and rainfall against years(1957-2019) visualisation for bradford and the comparison of trends between the two."
    "\ntype \033[1mAbdulla()\033[0m if you wish to see air frost and sun\n"
    "\ntype \033[1mJake()\033[0m if you wish to see average hours of sunlight against months\n"
    "\ntype \033[1mBenson()\033[0m if you wish to see rainfall against months data \n"
    "\ntype \033[1mPeter()\033[0m if you wish to see the correlation between sunshine and rain\n"
    "\ntype \033[1mMuhammad()\033[0m Minimum and Maximum temperature for aberpoth \n")
    if Visualisation == 'quit':
        break

    elif Visualisation.lower() == "joseph()":
        Joseph()

    elif Visualisation.lower()=="abdulla()":

        Abdulla()

    elif Visualisation.lower()=="jake()":

        Jake()   

    elif Visualisation.lower()=="benson()":   
        
        Benson()
        
    elif Visualisation.lower()=="peter()":   
        
        Peter()
    elif Visualisation.lower()=="muhammad()": 

        Muhammad()   

    else:
        print("There is no data matching this imput") 
        
        