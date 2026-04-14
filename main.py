from src.data_loader import load_data
from src.preprocessing import preprocess_data
from src.analysis import yearly_analysis
from src.visualization import plot_trend, plot_seaborn, plot_distribution
from src.anomaly_detection import detect_anomalies
from src.forecasting import forecast_temperature
import matplotlib.pyplot as plt


# STEP 1: Load data
df = load_data("data/raw/GlobalLandTemperaturesByCountry.csv")

# STEP 2: Preprocess
df = preprocess_data(df)

# STEP 3: Analysis
yearly = yearly_analysis(df)

# STEP 4: Visualization
plot_trend(yearly)
plot_seaborn(yearly)
plot_distribution(df)

# STEP 5: Anomaly Detection
yearly = detect_anomalies(yearly)

# Plot anomalies
plt.figure(figsize=(10,5))
plt.plot(yearly['year'], yearly['temperature'], label='Temperature')
plt.scatter(yearly[yearly['anomaly']==1]['year'],
            yearly[yearly['anomaly']==1]['temperature'],
            color='red', label='Anomaly')
plt.legend()
plt.title("Anomaly Detection")
plt.show()

# STEP 6: Forecasting
future_years, predictions = forecast_temperature(yearly)

plt.figure(figsize=(10,5))
plt.plot(yearly['year'], yearly['temperature'], label='Actual')
plt.plot(future_years, predictions, color='red', label='Predicted')
plt.legend()
plt.title("Future Temperature Prediction")
plt.show()