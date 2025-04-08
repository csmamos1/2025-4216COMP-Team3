import numpy as np 
import pandas as pd
import csv
import matplotlib.pyplot as plt

data=pd.read_csv('MET Office Weather Data.csv')
# imported do manipulate the grid ofr my visulaization

def joseph():

# I excluded the year 1965 bcause there was missing data values!
    new_data_Hurn = data[data["rain"].notna() & (data["station"]=="hurn") & 
                    (data["tmin"].notna())& (data["year"]!="1965.0")]
                
    #print (new_data)


   



    pd.set_option("display.max_rows", None)  # Show all rows
    pd.set_option("display.max_columns", None)  # Show all columns

    #print(new_data)


#although indices where present was getting empty column, problem could be after deleted rows so reconfigured indices
    new_data0 = new_data_Hurn.reset_index(drop=True)

    new_data1= new_data0[(new_data0["year"]<2020.0)]

    

    #print(len(new_data1)) # want to find how many months in total in my data set
    #after finding there 753months 753/12 gives float, means some years must have less months




    year_counts = new_data1["year"].value_counts()
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
    #issing_percentage = (missing_months / total_months) * 100
    #print(f"Missing Data Percentage: {missing_percentage:.2f}%")





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
            f" is {std_dev_tmin:.2f} celsius thus each point of data deviates from the mean(Minimum teperature between 1957-2019) by about {CV_tmin:.2f}% \n"
            f" which is a very negligible and shows a tight consistency between the data points \n"
            f" addiditonally there is a {missing_percentage:.2f}% error of the new data relative to the original")
    
    print(f"\n The average amount of rainfall from the years 1957-2019 in Hurn is \n  "
          f"{mean_rain_averages:.2f}mm and the standard deviation"
           f" (that is how much the the data deviates from the mean)\n"
            f" is {std_dev_rain:.2f}mm  thus each point of data deviates from the mean(Minimum teperature between 1957-2019) by about {CV_rain:.2f}% \n "
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
    ax.set_xticklabels(range_years, fontsize=8, rotation=45)  # Adjust fontsize and rotation
    ax.set_yticklabels(ax.get_yticks(), fontsize=8)
    ax.set_xlim(x.min()-1, x.max())  # delete extra space at the end of grid
    mean_val = np.mean(rain_averages)
    plt.axhline(mean_val, color='red', linestyle='--', linewidth=2, label='Mean')
    ax.legend()
    
   


    plt.show()



    fig, ax = plt.subplots()
    ax.plot(range_years, tmin_averages, 'mD:')
    ax.set_ylabel("Average Minimum temperature", color='m')
    ax1 = ax.twinx()
    ax1.plot(range_years, rain_averages, 'ro--')
    ax1.set_ylabel("Average rainfall", color='r')

    plt.show()

    print(f"{min(rain_averages):.2f}")
    print(f"{max(rain_averages):.2f}")



while True:
    Visualization = input("\n please type Joseph() to see rain against year visualization, " \
    "\n Aaverage minimum temperature against ye"
    "year visualization \n and average minimum temperature again")
    if Visualization == 'quit':
        break

    if Visualization.lower() == "joseph()":
        joseph()
    else:
        print("There is no data matching this imput")