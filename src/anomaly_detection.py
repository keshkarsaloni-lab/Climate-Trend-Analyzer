import numpy as np

def detect_anomalies(yearly_df):
    """
    Detect anomalies using Z-score
    """

    mean = yearly_df['temperature'].mean()
    std = yearly_df['temperature'].std()

    yearly_df['z_score'] = (yearly_df['temperature'] - mean) / std

    # Mark anomalies
    yearly_df['anomaly'] = yearly_df['z_score'].apply(lambda x: 1 if abs(x) > 2 else 0)

    return yearly_df