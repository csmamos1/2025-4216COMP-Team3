import pandas as pd
import matplotlib.pyplot as plt

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

# Run the function
Abdulla()
