import csv
import pandas as pd
import matplotlib.pyplot as plt


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

Benson()