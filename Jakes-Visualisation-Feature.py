import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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