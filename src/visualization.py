import matplotlib.pyplot as plt
import seaborn as sns

def plot_trend(yearly_df):
    """
    Plot temperature trend
    """

    plt.figure(figsize=(10,5))
    plt.plot(yearly_df['year'], yearly_df['temperature'], label='Temperature')
    plt.title("Temperature Trend Over Years")
    plt.xlabel("Year")
    plt.ylabel("Temperature")
    plt.legend()
    plt.show()


def plot_seaborn(yearly_df):
    """
    Better visualization using seaborn
    """

    plt.figure(figsize=(10,5))
    sns.lineplot(x='year', y='temperature', data=yearly_df)
    plt.title("Seaborn Trend Visualization")
    plt.show()


def plot_distribution(df):
    """
    Distribution of temperature
    """

    plt.figure(figsize=(8,5))
    sns.histplot(df['temperature'], kde=True)
    plt.title("Temperature Distribution")
    plt.show()