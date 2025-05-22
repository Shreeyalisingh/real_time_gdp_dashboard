import requests
import pandas as pd
import numpy as np

def fetch_gdp_data(country_code='IND'):
    url = f"http://api.worldbank.org/v2/country/{country_code}/indicator/NY.GDP.MKTP.CD?format=json&per_page=100"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception("Failed to fetch data")

    data = response.json()[1]  # the second element has the actual data
    records = []

    for entry in data:
        if entry['value'] is not None:
            records.append({
                'year': int(entry['date']),
                'gdp': float(entry['value'])
            })

    df = pd.DataFrame(records)
    df = df.sort_values(by='year')
    return df

def compute_growth_rates(df):
    df = df.copy()
    df['growth_rate (%)'] = df['gdp'].pct_change() * 100  # percentage growth
    df = df.dropna()
    return df

if __name__ == "__main__":
    gdp_df = fetch_gdp_data()
    gdp_with_growth = compute_growth_rates(gdp_df)
    print(gdp_with_growth.head())
