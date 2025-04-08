
import pandas as pd
import matplotlib.pyplot as plt






def Muhhammad():
    # Load the CSV file 
    file_path = "C:\\Users\isfah\\Coursework\\Coursework\\MET Office Weather Data.csv"
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