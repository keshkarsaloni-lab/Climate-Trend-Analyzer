import pandas as pd

def preprocess_data(df):
    """
    Clean and preprocess the data
    """

    # Convert date column
    df['dt'] = pd.to_datetime(df['dt'])

    # Extract year
    df['year'] = df['dt'].dt.year

    # Rename column (for simplicity)
    df = df.rename(columns={'AverageTemperature': 'temperature'})

    # Drop missing values
    df = df.dropna(subset=['temperature'])

    return df