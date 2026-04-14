from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_temperature(yearly_df):
    """
    Predict future temperature using Linear Regression
    """

    X = yearly_df['year'].values.reshape(-1,1)
    y = yearly_df['temperature'].values

    model = LinearRegression()
    model.fit(X, y)

    # Predict future (next 10 years)
    future_years = np.arange(yearly_df['year'].max()+1,
                             yearly_df['year'].max()+11).reshape(-1,1)

    predictions = model.predict(future_years)

    return future_years, predictions