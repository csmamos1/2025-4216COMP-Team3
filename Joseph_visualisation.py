import numpy as np 
import pandas as pd
import csv
import matplotlib.pyplot as plt

data=pd.read_csv('MET Office Weather Data.csv')
# imported do manipulate the grid ofr my visulaization

def joseph():

# I excluded the year 1965 bcause there was missing data values!
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
    #issing_percentage = (missing_months / total_months) * 100
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
    total_months = 63 * 12  # Expected months
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

    rain_range1=new_datax["rain"]
    rain_averages1=[]
    for start in range (0,748,12):
        end = start +12
        rain_averages1.append(rain_range1[start:end].sum()/12)

    std_dev_rain1=np.std(rain_averages1)
    std_dev_tmin1= np.std(tmin_averages1)
    mean_tmin_averages1= np.mean(tmin_averages1)
    mean_rain_averages1=np.mean(rain_averages1)
    CV_rain1= (std_dev_rain1/mean_rain_averages1)*100
    CV_tmin1= (std_dev_tmin1/mean_tmin_averages1)*100 
    total_months1 = 63 * 12  # Expected months
    missing_months1 = 8
    observed_months1 = total_months1 - missing_months1
    missing_percentage1 = (missing_months1 / total_months1) * 100

    #print(CV_rain1)










    print(f"\n The average minimum temperature from the years 1957-2019 in Hurn is \n  "
          f"{mean_tmin_averages:.2f} celcius, the coldest year was in" 
           f" 1962 which saw the coldest average minimum teperature of {min(tmin_averages):.2f}  and the standard deviation"
           f" (that is how much the the data deviates from the mean)\n"
            f" is {std_dev_tmin:.2f} celsius thus each point of data" 
            f"deviates from the mean(Minimum average teperature between 1957-2019) by about {CV_tmin:.2f}% \n"
            f" which is a very negligible and shows a tight consistency between the data points \n"
            f" addiditonally there is a {missing_percentage:.2f}% error of the new data relative to the original")
    
    print(f"\n The average amount of rainfall from the years 1957-2019 in Hurn is \n  "
          f"{mean_rain_averages:.2f}mm, the driest year was in 1973 which saw"
           f" the average rainfall of just {min(rain_averages):.2f}mm, while the wettest year was in 1960"
            f" which saw the average amount of rainfall of {max(rain_averages):.2f}mm  and the standard deviation"
           f" (that is how much the the data deviates from the mean)\n"
            f" is {std_dev_rain:.2f}mm  thus each point of data deviates"
             f" from the mean(Minimum teperature between 1957-2019) by about {CV_rain:.2f}% \n "
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